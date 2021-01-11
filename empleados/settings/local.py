
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'neuapp',
        'PASSWORD': 'neuapp',
        'HOST':'localhost',
        'PORT':'5433',
    }

  #'default': {
   #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'dbempleado',
   #     'USER': 'neuapp',
   #     'PASSWORD': 'neuapp',
   #     'HOST':'192.168.1.18',
   #     'PORT':'5432',
   # }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')] #indicao donde estaran los archivos estaticos y CSS del projecto

MEDIA_URL = '/media/'
MEDIA_ROOT= BASE_DIR.child('media') 