from .base import *

import os
import dj_database_url

from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = False


DATABASES = {
    'default': dj_database_url.config()
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2p2mp7tnuflmp',
        'USER': 'xbkfclhgeebjgn',
        'PASSWORD': '9ozQ2lfIVjkQ9K7GFpAAw_4X3c',
        'HOST': 'ec2-54-225-121-93.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
'''

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

#PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
#
# MEDIA_URL = '/media/'

# STATICFILES_STORAGE = "myproject.s3utils.StaticS3BotoStorage"
# DEFAULT_FILE_STORAGE = "myproject.s3utils.MediaS3BotoStorage"


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#STATIC_URL = '/static/'
# STATIC_ROOT = 'static/'

'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
'''


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'static/log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = 'admin@wiwik.online'
EMAIL_HOST_PASSWORD = '@Huntnhustle7'
DEFAULT_FROM_EMAIL = 'admin@wiwik.online'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Setup AWS S3 Bucket

AWS_STORAGE_BUCKET_NAME = 'whatiwishiknew'
AWS_ACCESS_KEY_ID = 'AKIAJ4B5DDEIUL2R3KEA'
AWS_SECRET_ACCESS_KEY = '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'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['posts'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]