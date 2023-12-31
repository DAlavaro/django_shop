import os
import smtplib
from email.mime.text import MIMEText

from django.conf import settings
from dotenv import load_dotenv

from django.db.models.signals import post_save
from django.dispatch import receiver

from reviews_app.models import Reviews

load_dotenv()

@receiver(post_save, sender=Reviews)
def post_signal(sender, instance, **kwargs):
    if instance.views_count >= 100:
        send_email(instance)

def send_email(instance):
    sender = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    message = f"Количество просмотров отзыва {instance.title} достигло 100!!!"
    server.login(sender, password)
    msg = MIMEText(message)
    msg["Subject"] = "Candle_shop"
    server.sendmail(sender, sender, msg.as_string())