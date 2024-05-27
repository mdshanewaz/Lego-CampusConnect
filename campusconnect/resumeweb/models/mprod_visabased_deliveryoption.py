#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_visabased import mprod_visabased
from .mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_visabased_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_visabased)
    class_threeletterprefix = "dd9"

    class Meta:
        verbose_name_plural = "08_Bandwidth_DelivOption_List"











