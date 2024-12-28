from celery import shared_task
from celery.utils.log import get_task_logger

from email_task.email import send_review_email

logger = get_task_logger(__name__)

@shared_task(name='send_mass_email_task')
def send_mass_email_task(name, email_list, review, pdf_file_path=None):
    logger.info(f"Task received: Sending email to {email_list}")
    logger.info(f"PDF file path: {pdf_file_path}")
    try:
        result = send_review_email(name, email_list, review, pdf_file_path)
        logger.info(f"Email sent, result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in send_mass_email_task: {str(e)}")
        raise