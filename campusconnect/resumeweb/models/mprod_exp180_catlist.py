from uuid import uuid4
from base64 import b64encode, b64decode
from dirtyfields import DirtyFieldsMixin

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

CHOISES = [('basic','basic'),('advanced','advanced'),]

# ******************************************************************************
class mprod_exp180_catlist(models.Model):
    catname = models.CharField(max_length=30, choices=CHOISES, default='basic')

    class Meta:
        verbose_name_plural = "01_exp180_Cat_List"

    def __str__(self):
        return "{}".format(self.catname)

