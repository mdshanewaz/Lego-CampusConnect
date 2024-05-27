#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_exp180 import mprod_exp180
from .mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_exp180_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_exp180)
    class_threeletterprefix = "dd3"

    class Meta:
        verbose_name_plural = "01_Exp180_DelivOption_List"














