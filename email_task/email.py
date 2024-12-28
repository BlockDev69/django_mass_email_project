from django.template.loader import render_to_string
from django.core.mail import send_mass_mail, EmailMessage
from django.conf import settings
import logging

import os

logger = logging.getLogger(__name__)

def send_review_email(name, email_list, review, pdf_file_path=None):
    logger.info(f"Preparing to send email to {email_list}")
    logger.info(f"PDF file path in send_review_email: {pdf_file_path}")
    context = {
        'name': name,  # Corrected from 'email' to 'name'
        'review': review,
    }
    email_subject = 'Thank you for your review'
    email_body = render_to_string('email_message.txt', context)

    try:
        for email in email_list:
            messages = EmailMessage(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )
            if pdf_file_path and os.path.exists(pdf_file_path):
                logger.info(f"Attaching PDF file: {pdf_file_path}")
                with open(pdf_file_path, 'rb') as pdf:
                    messages.attach(os.path.basename(pdf_file_path), pdf.read(), 'application/pdf')
            else:
                logger.warning(f"PDF file not found or not provided: {pdf_file_path}")
            messages.send(fail_silently=False)
        logger.info(f'Email sent sucessfully')
        return len(email_list)
    except Exception as e:
        logger.error(f'Error sending emails: {str(e)}')
        raise
    finally:
        # Suppression du fichier PDF temporaire
        if pdf_file_path and os.path.exists(pdf_file_path):
            os.remove(pdf_file_path)
            logger.info(f'Temporary PDF file deleted: {pdf_file_path}')