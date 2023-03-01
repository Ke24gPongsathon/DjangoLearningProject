from datetime import timedelta, time, datetime
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from django.core.mail import EmailMultiAlternatives
import os

# from orders.models import Order

today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send Today's Orders Report to User"
        
    def create_detail_txt(self):
        with open("detail.txt", "w+") as file:
            file.write(f"Testting file attaching. email sending date: {today.strftime('%d/%m/%Y')}")
            file.close()
        

    def handle(self, *args, **options):
        subject, from_email, to = 'Hello', 'noreply@djangolearningproject.com', 'gnekeng@gmail.com'
        text_content = 'This is an important message.'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        self.create_detail_txt()
        msg.attach_file("detail.txt")
        msg.send()
        
        
        # os.remove("detail.txt")