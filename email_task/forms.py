from django import forms
from email_task.tasks import send_mass_email_task

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.core.files.storage import default_storage
from django.conf import settings
import os

class Viewform(forms.Form):
    name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Prénom', 'id': 'fname'}
        )
    )
    emails = forms.CharField(
        label='Emails', widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mails (un par ligne)', 'rows': '3', 'id': 'emails'}
        )
    )
    review = forms.CharField(
        label='Review', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
    )
    pdf_file = forms.FileField(
        label='PDF File', required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )


    def clean_emails(self):
        emails = self.cleaned_data['emails'].split('\n')
        valid_emails = []
        for email in emails:
            email = email.strip()
            if email:
                try:
                    validate_email(email)
                    valid_emails.append(email)
                except ValidationError:
                    raise forms.ValidationError(f"L'email {email} n'est pas valide.")
        return valid_emails
    
    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get('pdf_file')
        if pdf_file:
            if not pdf_file.name.endswith('.pdf'):
                raise forms.ValidationError("Le fichier doit être au format PDF.")
            if pdf_file.size > 5*1024*1024:  # 5 MB limit
                raise forms.ValidationError("Le fichier ne doit pas dépasser 5 Mo.")
        return pdf_file

    def send_email(self, file_path=None):
        print("Sending email from form")
        pdf_file = self.cleaned_data['pdf_file']
        pdf_path = None

        if pdf_file:
            file_name = default_storage.save(pdf_file.name, pdf_file)
            pdf_path = os.path.join(settings.MEDIA_ROOT, file_name)

        send_mass_email_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['emails'],
            self.cleaned_data['review'],
            pdf_path
        )