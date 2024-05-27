from zzz_lib.zzz_log import zzz_print
from django.contrib import admin

from guestactions.models import (
    GuestResumeFiles,
    SiteSurveyModel,
    ContactUsModel,
)

from commonroom.models import (
    msendmail,
)

from resumeweb.models import mpaypal


@admin.register(mpaypal)
class AdminPaypal(admin.ModelAdmin):
    list_display = (
        "id",

    )


@admin.register(msendmail)
class Adminmsendmail(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
    )


@admin.register(GuestResumeFiles)
class admin_GuestResumeFiles(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "file1",
        "upload_time",
    )


@admin.register(SiteSurveyModel)
class AdminSiteSurvey(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at"
    )

