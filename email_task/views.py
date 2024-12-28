from django.shortcuts import render
from email_task.forms import Viewform
from django.views.generic.edit import FormView
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.core.files.storage import default_storage
import os
from django.conf import settings

# Create your views here.
class EmailView(FormView):
    template_name = 'review.html'
    form_class = Viewform

    def form_valid(self, form):
        pdf_file = form.cleaned_data['pdf_file']
        file_path = None

        if pdf_file:
            file_name = default_storage.save(pdf_file.name, pdf_file)
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)

        # Envoi de l'email avec le fichier PDF attaché si présent
        form.send_email(file_path)

        msg = 'Thanks for review'
        return HttpResponse(msg)

class HomeView(TemplateView):
    template_name='home.html'

    def home(request):
        pass
