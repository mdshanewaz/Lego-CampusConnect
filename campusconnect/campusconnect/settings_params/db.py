import os
from django.conf import settings


# DATABASES
###################################
if os.environ.get('SERVER_TYPE') == 'local':
  DATA_BASE_DIR = os.environ.get("DATA_BASE_DIR", settings.BASE_DIR)
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.sqlite3",
          "NAME": os.path.join(DATA_BASE_DIR, "db.sqlite3"),
      }
  }
else:
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "HOST": os.environ.get("RESUMEWEB_DBHOST"),
          "NAME": os.environ.get("RESUMEWEB_DBNAME"),
          "USER": os.environ.get("RESUMEWEB_DBUSERNAME"),
          "PASSWORD": os.environ.get("RESUMEWEB_DBPASS"),
          "PORT": os.environ.get("RESUMEWEB_DBPORT"),

      }
  }


## For testing purpose
## ************************************************
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "HOST": os.environ.get("RESUMEWEB_DBHOST"),
#         "NAME": os.environ.get("RESUMEWEB_DBNAME"),
#         "USER": os.environ.get("RESUMEWEB_DBUSERNAME"),
#         "PASSWORD": os.environ.get("RESUMEWEB_DBPASS"),
#         "PORT": os.environ.get("RESUMEWEB_DBPORT"),

#     }
# }
