#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .mprod_intprep import mprod_intprep
from .mbase_deliveryoption import mbase_deliveryoption

# ******************************************************************************
class mprod_intprep_deliveryoption(mbase_deliveryoption):
    products                = models.ManyToManyField(to=mprod_intprep)
    class_threeletterprefix = "dd4"

    class Meta:
        verbose_name_plural = "03_Dialogue_DelivOption_List"











