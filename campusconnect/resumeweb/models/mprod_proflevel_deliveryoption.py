#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_proflevel import mprod_proflevel
from .mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_proflevel_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_proflevel)
    class_threeletterprefix = "prf"

    class Meta:
        verbose_name_plural = "07_Staircase_DelivOption_List"











