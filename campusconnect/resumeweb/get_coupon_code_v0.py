from resumeweb.models import (mcoupon, mcoupon_given,)
from zzz_lib.zzz_log import zzz_print
from django.http import HttpResponse, HttpResponseRedirect
import requests

import logging
logger = logging.getLogger(__name__)


def send_coupon_code(email_address_list, product_line):

  # create an active mcoupon instance for any product line
  imcoupon = mcoupon.objects\
      .filter(product_liked=product_line,active=True)\
      .order_by('-discount_percent')\
      .first()
  # print('--------------------------------------------------------------------------')
  # print('value of imcoupon>>>{}'.format(imcoupon))
  # print('--------------------------------------------------------------------------')

  if not imcoupon:
      zzz_print("    %-28s: %s" % ("coupon creation by force FAILED", "mprod_exp180"))
      # redirect user to page 404 error page
      return HttpResponse('someting is wrong from line#99')

  else:
    zzz_print("   %s " % ("ACTIVE MCOUPON FOUND"))

    # generate coupon code for each email
    coupon_code = []
    for i in email_address_list:
        imcoupon_given = mcoupon_given.objects.mcoupon_given_add(request=request, mcoupon=imcoupon)
        imcoupon_given = imcoupon_given.random_string_32
        coupon_code.append(imcoupon_given)


    # send email to submitter(guest) with a coupon code from coupon_code
    context = {
        'discount_percent'  : imcoupon.discount_percent,
        'hours_to_expire'   : imcoupon.hours_to_expire,
        'random_string_32'  : coupon_code[0],
        'email_guest'       : email_guest,
        'email_friend'      : email_friend,
    }

    plain_message_text = render_to_string(TEMP_DIR_EMAIL+'to_guest/' + 'email_with_coupon_plain.html', context)
    html_message_text  = render_to_string(TEMP_DIR_EMAIL+'to_guest/' + 'email_with_coupon_html.html', context)
    # zzz_print("    %-28s: %s" % ("plain_message_text", plain_message_text))
    # zzz_print("    %-28s: %s" % ("html_message_text", html_message_text))

    to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
    to_emails_list.append(email_guest)

    imsendmail = msendmail.objects.add(
        subject             = form.cleaned_data["guest_first_name"] + ", thanks for inviting your friends!",
        plain_message       = plain_message_text,
        html_message        = html_message_text,
        from_email          = settings.EMAIL_HOST_USER,
        to_emails_list      = to_emails_list
    )
    imsendmail.send_to_each_recipient_seperately()


    # send email to friend with a coupon code from coupon_code
    context = {
        'discount_percent'  : imcoupon.discount_percent,
        'hours_to_expire'   : imcoupon.hours_to_expire,
        'random_string_32'  : coupon_code[1],
        'email_guest'       : email_guest,
        'email_friend'      : email_friend,
    }

    plain_message_text = render_to_string(TEMP_DIR_EMAIL+'to_friend/' + 'email_with_coupon_plain.html', context)
    html_message_text  = render_to_string(TEMP_DIR_EMAIL+'to_friend/' + 'email_with_coupon_html.html', context)
    # zzz_print("    %-28s: %s" % ("plain_message_text", plain_message_text))
    # zzz_print("    %-28s: %s" % ("html_message_text", html_message_text))

    to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
    to_emails_list.append(email_friend)

    imsendmail = msendmail.objects.add(
        subject             = form.cleaned_data["friend_first_name"] + ", you have an invitation!",
        plain_message       = plain_message_text,
        html_message        = html_message_text,
        from_email          = settings.EMAIL_HOST_USER,
        to_emails_list      = to_emails_list
    )
    imsendmail.send_to_each_recipient_seperately()   


def send_coupon_code_v0(email_address_list, product_line):

  # create an active mcoupon instance for any product line
  imcoupon = mcoupon.objects\
      .filter(product_liked=product_line,active=True)\
      .order_by('-discount_percent')\
      .first()
  # print('--------------------------------------------------------------------------')
  # print('value of imcoupon>>>{}'.format(imcoupon))
  # print('--------------------------------------------------------------------------')

  if not imcoupon:
      zzz_print("    %-28s: %s" % ("coupon creation by force FAILED", "mprod_exp180"))
      # redirect user to page 404 error page
      return HttpResponse('someting is wrong from line#99')

  else:
    zzz_print("   %s " % ("ACTIVE MCOUPON FOUND"))

    # generate coupon code for each email
    coupon_code = []
    for i in email_address_list:
        imcoupon_given = mcoupon_given.objects.mcoupon_given_add(request=request, mcoupon=imcoupon)
        imcoupon_given = imcoupon_given.random_string_32
        coupon_code.append(imcoupon_given)


    # send email to submitter(guest) with a coupon code from coupon_code
    context = {
        'discount_percent'  : imcoupon.discount_percent,
        'hours_to_expire'   : imcoupon.hours_to_expire,
        'random_string_32'  : coupon_code[0],
        'email_guest'       : email_guest,
        'email_friend'      : email_friend,
    }

    plain_message_text = render_to_string(TEMP_DIR_EMAIL+'to_guest/' + 'email_with_coupon_plain.html', context)
    html_message_text  = render_to_string(TEMP_DIR_EMAIL+'to_guest/' + 'email_with_coupon_html.html', context)
    # zzz_print("    %-28s: %s" % ("plain_message_text", plain_message_text))
    # zzz_print("    %-28s: %s" % ("html_message_text", html_message_text))

    to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
    to_emails_list.append(email_guest)

    imsendmail = msendmail.objects.add(
        subject             = form.cleaned_data["guest_first_name"] + ", thanks for inviting your friends!",
        plain_message       = plain_message_text,
        html_message        = html_message_text,
        from_email          = settings.EMAIL_HOST_USER,
        to_emails_list      = to_emails_list
    )
    imsendmail.send_to_each_recipient_seperately()


    # send email to friend with a coupon code from coupon_code
    context = {
        'discount_percent'  : imcoupon.discount_percent,
        'hours_to_expire'   : imcoupon.hours_to_expire,
        'random_string_32'  : coupon_code[1],
        'email_guest'       : email_guest,
        'email_friend'      : email_friend,
    }

    plain_message_text = render_to_string(TEMP_DIR_EMAIL+'to_friend/' + 'email_with_coupon_plain.html', context)
    html_message_text  = render_to_string(TEMP_DIR_EMAIL+'to_friend/' + 'email_with_coupon_html.html', context)
    # zzz_print("    %-28s: %s" % ("plain_message_text", plain_message_text))
    # zzz_print("    %-28s: %s" % ("html_message_text", html_message_text))

    to_emails_list = copy.deepcopy(settings.DEVELOPMENT_ONLY_EMAIL_RECIPIENTS)
    to_emails_list.append(email_friend)

    imsendmail = msendmail.objects.add(
        subject             = form.cleaned_data["friend_first_name"] + ", you have an invitation!",
        plain_message       = plain_message_text,
        html_message        = html_message_text,
        from_email          = settings.EMAIL_HOST_USER,
        to_emails_list      = to_emails_list
    )
    imsendmail.send_to_each_recipient_seperately()   
