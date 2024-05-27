from zzz_lib.zzz_log import zzz_print
from django.db import models
from .mbase_prod import mbase_prod
from .. import const_resumeweb
from .mprod_exp180_catlist import mprod_exp180_catlist


# ******************************************************************************
class mprod_exp180(mbase_prod):
    # Note: fields listprice, saleprice and sku defined in parent classes
    title               = models.CharField(max_length=500)
    description         = models.TextField(blank=False, null=False)
    deliverables        = models.TextField(blank=True, null=True)
    serv_cat            = models.CharField(max_length=200, choices=const_resumeweb.SERVICE_CATEGORY, default='analysis')
    golivestatus        = models.CharField(max_length=20, choices=const_resumeweb.GOLIVE_STATUS, default='draft')
    trending            = models.CharField(max_length=10, choices=const_resumeweb.TRENDING, default='no')
    homepage_showup     = models.CharField(max_length=20, choices=const_resumeweb.HOMEPAGE_SHOWUP, default='no')
    level               = models.CharField(max_length=20, choices=const_resumeweb.EXP180LEVEL, default='others')
    category            = models.ForeignKey(mprod_exp180_catlist, on_delete=models.CASCADE, null=True)

    class_threeletterprefix = "exp"

    class Meta:
        verbose_name_plural = "01-Exp180-services"

    # --------------------------------------------------------------------------
    def __str__(self):
        return f'{self.sku}, {self.category}, {self.title}'

    # # --------------------------------------------------------------------------
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

