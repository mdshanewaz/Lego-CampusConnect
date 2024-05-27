from django import forms
from django.forms import Textarea
from ..models import (
	DisputeClaim,
	DispCause
)
from resumeweb.models import mcart
from django.contrib.auth.models import User




class DisputeForm(forms.ModelForm):

	class Meta:
		model = DisputeClaim
		fields = "__all__"
		exclude = ('created_aganist', 'created_by',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""


