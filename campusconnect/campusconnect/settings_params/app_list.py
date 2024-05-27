# INSTALLED APPS
################

PREREQ_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "widget_tweaks",
    "crispy_forms",
    "django.contrib.postgres",
    "django_elasticsearch_dsl",
    "django_elasticsearch_dsl_drf",
    # 'django_redis',
    # "storages",
    # "debug_toolbar",    

]

CUSTOM_APPS = [
    "adhoc",
    "mmhauth",
    "commonroom",
    "guestactions",
    "mydocumentations",
    "prof_candidate",
    "resumeweb",
    "superadmin",
    "viewtracker",
    
]

INSTALLED_APPS = PREREQ_APPS + CUSTOM_APPS

