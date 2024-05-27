from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from uuid import uuid4
from base64 import b64encode, b64decode

from dirtyfields import DirtyFieldsMixin

# ******************************************************************************
class mprod_visabased_list(models.Model):
    visaname = models.CharField(max_length=20, unique=True, null=False)

    class Meta:
        verbose_name_plural = "08_Bandwidth_Cat_List"

    def clean_name(self):
        return self.cleanned_data["visaname"].lower()

    def __str__(self):
        return "{}".format(self.visaname)

    def save(self, force_insert=False, force_update=False):
        self.visaname=self.visaname.lower()
        super(mprod_visabased_list, self).save(force_insert, force_update)






