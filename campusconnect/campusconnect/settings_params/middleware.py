# MIDDLEWARE
############

MIDDLEWARE_PRE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'admin_reorder.middleware.ModelAdminReorder',
]

MIDDLEWARE_CUSTOM = [
    "viewtracker.middleware.mw_viewTracker",
    "resumeweb.middleware.mw_mmhUserUniqueid",
]

MIDDLEWARE = MIDDLEWARE_PRE + MIDDLEWARE_CUSTOM
