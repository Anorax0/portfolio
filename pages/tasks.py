import os
import logging
from celery import shared_task
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_FROM_EMAIL = os.environ.get("SENDGRID_FROM_EMAIL", None)
SENDGRID_TO_EMAIL = os.environ.get("SENDGRID_TO_EMAIL", None)
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", None)

log = logging.getLogger(__name__)


@shared_task()
def send_email_task(name: str, message: str) -> str:
    try:
        message = Mail(
            from_email=SENDGRID_FROM_EMAIL,
            to_emails=SENDGRID_TO_EMAIL,
            subject=f"You have unread message from {name}",
            html_content=f"<h2>Message from {name}:</h2>" f"{message}",
        )
        try:
            sendgrid = SendGridAPIClient(SENDGRID_API_KEY)
            sendgrid.send(message)
            return "Email send"
        except Exception as e:
            log.error("Cannot send e-mail due to error in task: ", e)

    except Exception as e:
        log.error("Error: Cannot send e-mail due to error in task: ", e)
