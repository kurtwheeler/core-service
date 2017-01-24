"""
Django settings for cognoma_site project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# The warning below is usually correct, but we do not use this secret key in this project
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x!w(6=d6#)yl0ne8yhv#2+*+_nk7vf0#peh4hehg$&83fp^u01'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [os.getenv('DJANGO_HOST', '*')]


# Application definition

DJANGO_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
]

LOCAL_APPS = [
    'api.apps.ApiConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'api.auth.CognomaAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        # JSON as primary renderer for API functionality
        'rest_framework.renderers.JSONRenderer',
        # Support HTML / web browsable renderer for interacting with API
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

MIDDLEWARE_CLASSES = [
]

ROOT_URLCONF = 'cognoma_site.urls'

WSGI_APPLICATION = 'cognoma_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        'HOST': os.getenv('DB_HOST', 'core_db'),
        'PORT': os.getenv('DB_PORT', '5432')
    }
}

dev_pub_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5knVYXDKNZAZ36TAo2S2
it2PkkzlulB8jlLXIo9fOd6NV/v1gp3AUb3yz8otAa9lV5DKQvGUhkVe3dhfHNPv
nL1w+x/4evi6qXnvbuJ+vlNcaJrSWFAvx8CFSRfUMnyACT7WDwkJZFYYWzTTBhzZ
fE9D4/DtyrHhZFiB8xjAUbVmBO6f7zwp41Ehr11s5SokweYytwQy38AFvwGUOM6P
AeN+7bMBi4PfTr4Y4VN/93OBckj4Dfe6AEtq31Z5Urh/e/+zaixbsmenAR1hvC6Z
34+qca3WMUIZjdeIny4XP0xhzbZNP66tNqUBkJg/fkhKVEeFMHaQ7giBTtqMnXPz
6wIDAQAB
-----END PUBLIC KEY-----
"""
# SECURITY WARNING: change this to the prod public key!!
JWT_PUB_KEY = os.getenv('JWT_PUB_KEY', dev_pub_key)

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Extra static assets that aren't tied to an app
STATICFILES_DIRS = [
]
