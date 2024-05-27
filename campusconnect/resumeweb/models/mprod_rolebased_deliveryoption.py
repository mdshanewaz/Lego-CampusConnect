#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_rolebased import mprod_rolebased
from .mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_rolebased_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_rolebased)
    class_threeletterprefix = "dd7"

    class Meta:
        verbose_name_plural = "06_Identity_DelivOption_List"





