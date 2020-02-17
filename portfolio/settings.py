"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import dj_database_url

# # SECURITY WARNING: don't run with debug turned on in production!
try:
    from .local_settings import *
except:
    DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'gallery.apps.GalleryConfig',
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

if not DEBUG:
    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
        }
    }
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'portfolio/static')]

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success'
}

# Crispy setting
CRISPY_TEMPLATE_PACK = 'bootstrap4'

if not DEBUG:
    DARKSKY_API_KEY = os.environ.get('DARKSKY_API_KEY_VALUE')


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'portfolio.storage.WhiteNoiseStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True


django_heroku.settings(locals())

if not DEBUG:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_REGION_NAME = 'eu-west-3'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_QUERYSTRING_AUTH = False

import boto
from boto.s3.connection import S3Connection

use_sigv4 = boto.config.get('s3', 'use-sigv4')
if not use_sigv4:
    boto.config.add_section('s3')
    boto.config.set('s3', 'use-sigv4', 'True')


conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, host='s3.eu-west-3.amazonaws.com')
bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)

# restore the signature version, if it applies
if not use_sigv4:
    boto.config.remove_section('s3')

if not DEBUG:
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
if not DEBUG:
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = os.environ.get('EMAIL_PORT')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
    EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL')
    EMAIL_RECEIVER = os.environ.get('EMAIL_RECEIVER')
