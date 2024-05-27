from zzz_lib.zzz_log import zzz_print
import json
from uuid import uuid4
from datetime import datetime
from django.shortcuts import render
from base64 import b64decode, b64encode
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import connection
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic.edit import CreateView

from commonroom.myfunctions.send_email import send_email_customized
import datetime
from django.db.models.functions import Substr

from django.views.generic import (
    ListView,
    UpdateView,
    DetailView
)
from django.contrib.auth.decorators import login_required
from django.conf import settings


from resumeweb.models import (
    mcart
)

from ..models import (
    DisputeClaim,
)


from ..forms import (
    DisputeForm
)


TEMPLATE_DIR = "prof_candidate/layout/disputes/"


# file a dispute
# where customer will be able to submit a dispute aganist an order that is already selected
import datetime
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404
# ******************************************************************************
class FileDisputeWithTrackingId(LoginRequiredMixin,CreateView):
    template_name = TEMPLATE_DIR + "aganist_order.html"
    # form = DisputeForm()
    model = DisputeClaim
    fields = ['created_aganist', 'dispcause', 'msg']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.created_at = datetime.datetime.now()

        self.object.save()

        form.save_m2m()


        subject = "File dispute"
        email_body = "You have successfully filled a dispution"   
        time = datetime.datetime.now()     
        send_email_customized(self.request.user,subject,email_body,time)
        return redirect('prof_candidate:dispute_confirm')

        
    # def post(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         form = DisputeForm(request.POST or None)
    #         if form.is_valid():
    #             p = form.save(commit=False)
    #             p.created_by = self.request.user
    #             p.created_at = datetime.datetime.now()
    #             # p.created_aganist = mcart.objects.get(id=self.kwargs['id'])
    #             p.save()
    #             form.save_m2m()
    #             print(self.request.user)
    #             subject = "File dispute"
    #             email_body = "You have successfully disputed a file"    
    #             time = datetime.datetime.now()    
    #             send_email_to_user(self.request.user.email,subject,email_body,time)
    #             return redirect('prof_candidate:dispute_confirm')
    #     else:
    #         form = Dispute()

    # def get_queryset(self):
    #     zzz_print("    %-28s: %s" % ("get_queryset()", ""))
    #     # self.id = get_object_or_404(mcart, id=self.kwargs['id'])
    #     qs = mcart.objects.all()
    #     # qs = mcart.objects.filter(id=self.kwargs['id'])

    #     return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = DisputeForm()
    #     return context






class FileDisputeFromOrderDetails(LoginRequiredMixin, CreateView):
    template_name = TEMPLATE_DIR + "aganist_order.html"
    form_class = DisputeForm
    # model = Dispute
    # fields = ['dispcause', 'msg']
    

    # def get_queryset(self):
    #     zzz_print("    %-28s: %s" % ("get_queryset()", ""))
    #     # self.id = get_object_or_404(mcart, id=self.kwargs['id'])
    #     qs = mcart.objects.all()
    #     # qs = mcart.objects.filter(id=self.kwargs['id'])

    #     return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DisputeForm()
        context['pgheader'] = "Dispute Against Order"
        context['track_id'] = self.kwargs['tracking_id']
        
        return context


    # def post(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         form = DisputeForm(request.POST or None)
    #         if form.is_valid():
    #             p = form.save(commit=False)
    #             p.created_by = self.request.user
    #             p.created_at = datetime.datetime.now()
    #             # p.created_aganist = mcart.objects.get(id=self.kwargs['id'])
    #             # p.created_aganist = form.cleaned_data['created_aganist']

    #             p.save()
    #             form.save_m2m()
    #             return redirect('prof_candidate:dispute_confirm')
    #     else:
    #         form = Dispute()



    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.created_at = datetime.datetime.now()
        self.object.created_aganist = self.kwargs['tracking_id']
        print(self.object.created_aganist)
        self.object.save()
        print(form)
        form.save_m2m()
        
        
        # subject = "File dispute"
        # email_body = f"You have successfully filled a dispution of {self.tracking id}"   
        # time = datetime.datetime.now()     
        # send_email_to_user(self.request.user,subject,email_body,time)

        return redirect('prof_candidate:dispute_confirm')
        # return HttpResponse("Form Submitted")







# file a dispute
# where customer will be able to submit a dispute aganist an order that is not selected yet
# ******************************************************************************
# class FileDispute(CreateView):
#     template_name = TEMPLATE_DIR + "aganist_order.html"
#     # form = DisputeForm()
#     model = Dispute
#     fields = ['created_aganist', 'dispcause', 'msg']

#     def post(self, request, *args, **kwargs):
#         if request.method == "POST":
#             form = DisputeForm(request.POST or None)
#             if form.is_valid():
#                 p = form.save(commit=False)
#                 p.created_by = self.request.user
#                 p.created_at = datetime.datetime.now()
#                 # p.created_aganist = mcart.objects.get(id=self.kwargs['id'])
#                 p.save()
#                 form.save_m2m()
#                 return redirect('prof_candidate:dispute_confirm')
#         else:
#             form = Dispute()

    # def get_queryset(self):
    #     zzz_print("    %-28s: %s" % ("get_queryset()", ""))
    #     # self.id = get_object_or_404(mcart, id=self.kwargs['id'])
    #     qs = mcart.objects.all()
    #     # qs = mcart.objects.filter(id=self.kwargs['id'])

    #     return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = DisputeForm()
    #     return context




# ******************************************************************************
class DisputeConfirmation(LoginRequiredMixin,ListView):
    model = DisputeClaim
    template_name = TEMPLATE_DIR + "disp_conf.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(created_by=self.request.user)\
            .order_by('-created_at')



# ******************************************************************************
# Response from TMS/DisputeResolutionCenter 
# ******************************************************************************

class DisputeResult(LoginRequiredMixin, ListView):
    model = DisputeClaim
    template_name = TEMPLATE_DIR + "results.html"

# for decision date sample code
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms







class DisputeHistory(LoginRequiredMixin,ListView):
    model = DisputeClaim
    template_name = TEMPLATE_DIR + "history.html"

    def get_queryset(self):
        zzz_print("    %-28s: %s" % ("get_queryset()", ""))
        qs = DisputeClaim.objects.all().order_by('created_by').order_by('-created_at')

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        zzz_print("    %-28s: %s" % ("get_context_data()", ""))
        context = super().get_context_data(**kwargs)

        context["no_of_disputes"] = DisputeClaim.objects.count()
        context['pgheader'] = "My Dispute History"
        for key in context:
            zzz_print("    key %-24s: value %s" % (key, context[key]))

        return context




# ******************************************************************************
class DisputeDetails(LoginRequiredMixin, DetailView):
    model = DisputeClaim
    template_name = TEMPLATE_DIR + "details.html"

    # def get_context_data(self, **kwargs):
    #     sys_user = self.request.user
    #     disp_details = Dispute.objects.filter(created_by=sys_user)[3]
    #     print("id ",disp_details.dispcause.all)

    




    # queryset = Dispute.objects.all_with_prefetch_dispcause()


    # def get_queryset(self):
    #     this is correct
    #     qs = Dispute.objects.get(id=self.kwargs['id'])
    #     return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # context['disp_causes'] = Dispute.objects.get(id=self.kwargs['id']).dispcause.all()
        # context = {
        #     'pgheader': 'Dispute Details'
        # }
    #     return context


