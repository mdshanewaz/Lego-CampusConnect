from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from uuid import uuid4
from base64 import b64encode, b64decode

from dirtyfields import DirtyFieldsMixin

# ******************************************************************************
class mprod_rolebased_list(models.Model):
    rolename = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "06_Identity_Cat_List"

    def __str__(self):
        return "{}".format(self.rolename)




