from datetime import datetime
import copy

from django.db.models import Q
from itertools import chain

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from zzz_lib.zzz_log import zzz_print
from ..models import mfeedback
from resumeweb.models import mcoupon, mcoupon_given
from resumeweb.models import msendmail

from ..forms import ProductReviewForm

from resumeweb.send_email_with_coupon_code import send_email
from resumeweb.get_coupon_code import generate_coupon_code
from commonroom.myfunctions.send_email import send_email_customized
from django.utils.html import strip_tags

TEMP_DIR_GENERAL        = 'resumeweb/layout/general/'
TEMP_DIR_ACTION         = 'guestactions/product-review/'
TEMP_DIR_CONF           = 'resumeweb/layout/'
TEMP_DIR_PRODABOUT      = 'resumeweb/layout/product-docs/'
TEMP_DIR_EMAIL          = 'commonroom/general/'
TEMP_DIR_PRODFEEDBACK   = 'resumeweb/layout/guest-actions/product-review/'

import datetime
# product review system homepage
# ************************
def ProductReviewGuestView(request):
  zzz_print("    %-28s: %s" % ("ProductReviewGuestView", "********************"))

  if request.method == "POST":
    form = ProductReviewForm(data=request.POST)

    if form.is_valid():
        zzz_print("    %-28s: %s" % ("form.is_valid", ""))

        # at first, save user given email add in a var 
        user_email_add = form.cleaned_data["email_address"]
        # save user_email_add in a session variable to be used in another view
        request.session['user_email_add'] = user_email_add

        # save user given form data in db 
        imfeedback = mfeedback.objects.add_mfeedback(
            request         = request,
            first_name      = form.cleaned_data["first_name"],
            last_name       = form.cleaned_data["last_name"],
            email_address   = form.cleaned_data["email_address"],
            product_liked   = form.cleaned_data["product_liked"],
            feedback        = form.cleaned_data["feedback"],
        )
        zzz_print("    %-28s: %s" % ("imfeedback", imfeedback))

        # generate/select a coupon code from coupon table
        product_line = form.cleaned_data["product_liked"]
        cop_code = generate_coupon_code(product_liked=product_line)
        if cop_code is not None:
          cop_code = "No coupon code added"

        # send email to the user
        appname = "GENERAL"
        subject = "Resumenalyzer Product Review Submission Confirmation"
        to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
        to_emails_list.append(user_email_add)
        email_context = {
            'change_notice'     : 'reviewing our product',
            'submission_time'   : datetime.datetime.now(),
            'msg'               : 'thanks for your contacting us',
            'coupon_code_dict'  : cop_code,
        }
        html_message_text = render_to_string(
            template_name=TEMP_DIR_EMAIL + 'common.html',
            context=email_context,
            using=None,
            request=None
        )
        plain_message_text = strip_tags(html_message_text)
        print("calling send_email_customized")
        send_email_customized(subject, plain_message_text, html_message_text, to_emails_list, appname)
        # email function ends

        # redirect user to thankyou page
        return redirect("feedback_submit_confirmation_view")
    else:
        zzz_print("    %-28s: %s" % ("NOT form.is_valid", ""))
  else:
      zzz_print("    %-28s: %s" % ("request.method", "!= POST"))
      form = ProductReviewForm()

  template_name   = TEMP_DIR_ACTION + "home.html"
  context         = {
    "form": form,
    "pg_headline": "Submit Product Review",
    "resp_time": "1"
  }
  
  return render(
      request = request, 
      template_name = template_name, 
      context = context
  )


# confirmation page
# *****************
def feedback_submit_confirmation_view(request):
  zzz_print("    %-28s: %s" % ("feedback_submit_confirmation_view", "********************"))
  template_name  = TEMP_DIR_PRODFEEDBACK + "confirmation.html"

  email_add = request.session.get('user_email_add')
  
  context = {
      "email_address":  email_add,
      "date_time":      datetime.datetime.now(),
      "blue":           "blue",
      "red":            "red",
      "task":           "Product Review"
  }
  return render(
      request = request, 
      template_name = template_name, 
      context = context
  )
