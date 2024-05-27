import debug_toolbar
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings


from prof_candidate.views import resume_download_view

urlpatterns = [

    # app name >> adhoc
    ##############################################
    path("app/adhoc/", include('adhoc.urls')),

    # app name >> mmhauth
    ##############################################
    path('app/auth_mmh/v2/', include('mmhauth.urls')),

    # app name >> guestactions
    ##############################################
    path('app/actions/', include('guestactions.urls')),

    # app name >> mydocumentations
    ##############################################
    path('app/docs/', include('mydocumentations.urls')),

    # app name >> prof_candidate
    ##############################################
    path('app/candidate/', include('prof_candidate.urls')),

    # app name >> resumeweb
    ##############################################
    path('',    include('resumeweb.urls')),
    path('rw/', include('resumeweb.urls')),
    
    # app name >>> superadmin
    ##############################################
    path('app/superadmin/', include('superadmin.urls')),




    # debug toolbar
    # path('__debug__/', include(debug_toolbar.urls)),




    # file download
    ##############################################
    path('download/', resume_download_view, name="resume_download_link"),



]
