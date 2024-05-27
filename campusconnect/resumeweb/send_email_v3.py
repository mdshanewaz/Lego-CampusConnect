from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, BadHeaderError
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from resumeweb.get_coupon_code import generate_coupon_code

from resumeweb.models import msendmail


def send_email(subject, plain_message_text, html_message_text, to_emails_list, appname):

    if to_emails_list is not None:
        imsendmail = msendmail.objects.add(
            subject             = subject,
            plain_message       = plain_message_text,
            html_message        = html_message_text,
            from_email          = settings.EMAIL_CONFIG["SHOPCART"]["EMAIL_HOST_USER"],
            to_emails_list      = to_emails_list,
            appname             = appname
        )
        imsendmail.send_to_each_recipient_seperately()
        print("email sent from send_email_v3.py file")
    else:
        print("email sending has failed")
