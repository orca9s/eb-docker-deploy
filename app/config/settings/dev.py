from .base import *

DEBUG = True


WSGI_APPLICATION = 'config.wsgi.dev.application'

ALLOWED_HOSTS = []

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

STATIC_URL = '/static/'