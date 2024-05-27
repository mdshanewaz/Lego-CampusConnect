from datetime import datetime

from django.db.models import Q
from itertools import chain

# from haystack.query import SearchQuerySet 
import datetime
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from zzz_lib.zzz_log import zzz_print
from ..models import ContactUsModel

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

import logging
logger = logging.getLogger(__name__)

from ..forms import ContactUsForm

from django.template import Context
from django.core.mail import send_mail, BadHeaderError
RESUME_FILE_TYPES = ['doc', 'docx']
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.edit import FormMixin


import datetime
from django.http import HttpResponse


from django.views.generic.edit import FormView
from commonroom.myfunctions.send_email import send_email_customized
import copy


TEMP_DIR_ACTION         = 'guestactions/contact-us/'
TEMP_DIR_EMAIL          = 'commonroom/general/'


class ContactUsGuestView(FormView):
    template_name = TEMP_DIR_ACTION + "home.html"
    form_class = ContactUsForm
    success_url = reverse_lazy('guestactions:contact_us_guest')
    success_msg = "You message has been received successfully"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
        

class ContactUsGuestConfirmView(TemplateView):
    template_name = TEMP_DIR_ACTION + "contact-us-confirm.html"
