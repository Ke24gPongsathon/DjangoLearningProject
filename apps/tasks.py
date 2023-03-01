from celery import shared_task
from django.core.management import call_command

from celery import Task

@shared_task
def periodic_email_report():
    print("The sample task just ran.")
    call_command("periodic_email_report")
