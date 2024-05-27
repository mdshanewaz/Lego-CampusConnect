#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_proglang import mprod_proglang
from .mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_proglang_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_proglang)
    class_threeletterprefix = "prg"

    class Meta:
        verbose_name_plural = "05_Dialect_DelivOption_List"










