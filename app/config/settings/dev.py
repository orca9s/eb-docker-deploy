from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

ALLOWED_HOSTS = []

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))
DATABASES = secrets['DATABASES']

STATIC_URL = '/static/'