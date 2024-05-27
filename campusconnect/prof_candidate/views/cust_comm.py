import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from prof_candidate.models import (
    CandidateInternalMsg,
)
from zzz_lib.zzz_log import zzz_print
from ..forms import CandidateInternalMsgForm
from commonroom.myfunctions.send_email import send_email_customized


TEMPLATE_DIR = "prof_candidate/layout/cust_comm/"


# ******************************************************************************
class CandidateMsg(LoginRequiredMixin, CreateView):
    template_name = TEMPLATE_DIR + "contact-us.html"
    form_class = CandidateInternalMsgForm

    def form_valid(self, form):
        m = form.save(commit=False)
        m.created_by = self.request.user
        m.created_at = datetime.datetime.now()
        m.save()
        subject = "We are here to listen you "
        email_body = "Thank You for contacting us. Our resposible person will contact you soon"     
        time = datetime.datetime.now()   
        
        send_email_customized(self.request.user.email,subject,email_body,time)
        return HttpResponseRedirect(reverse('prof_candidate:msg_confirm'))


# ******************************************************************************
class MsgHistory(LoginRequiredMixin, ListView):
    model = CandidateInternalMsg
    template_name = TEMPLATE_DIR + "msg-history.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        zzz_print("    %-28s: %s" % ("get_context_data()", ""))

        context = super().get_context_data(**kwargs)
        context["no_of_msg"] = CandidateInternalMsg.objects.filter(created_by=self.request.user).count()
        for key in context:
            zzz_print("    key %-24s: value %s" % (key, context[key]))

        return context

    def get_queryset(self):
        qs = CandidateInternalMsg.objects.filter(created_by=self.request.user)\
            .order_by('-created_at')
        return qs



# ******************************************************************************
class MsgDetails(LoginRequiredMixin, DetailView):
    model = CandidateInternalMsg
    template_name = TEMPLATE_DIR + "msg-details.html"



# ******************************************************************************
class MsgConfirm(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_DIR + "msg_confirm.html"

