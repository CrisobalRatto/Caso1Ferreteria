import os
import warnings
from django.utils.translation import ugettext_lazy as _
from os.path import dirname
#import posixpath

warnings.simplefilter('error', DeprecationWarning)

BASE_DIR = dirname(dirname(os.path.abspath(__file__)))

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
#C:\Users\Cris20xx\source\repos\CrisobalRatto\Caso1Ferreteria\caso1ferreteria\content\

SECRET_KEY = 'e81a1891-b28b-4b00-b5a7-af0a0e216df9'

DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 
    'bootstrap4',

    # Application apps
    'accounts',
    'main',
    'app',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'caso1ferreteria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CONTENT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'caso1ferreteria.wsgi.application'

#mail settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = os.path.join(CONTENT_DIR, 'tmp/emails')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cristofopo@gmail.com'
EMAIL_HOST_PASSWORD = 'frffirnuzcbeukcu' 
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'

#EMAIL_HOST = 'smpt.gmail.com'
#EMAIL_PORT = '587'
#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = os.path.join(CONTENT_DIR, 'tmp/emails')
#EMAIL_HOST_USER = 'cristofopo@gmail.com'
#EMAIL_HOST_PASSWORD = 'frffirnuzcbeukcu'
#DEFAULT_FROM_EMAIL = 'cristofopo@gmail.com'
#EMAIL_USE_TLS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'orcl',
        'USER': 'C##FERME',
        'PASSWORD': 'asd',
        'TEST': {
            'USER': 'default_test',
            'TBLSPACE': 'default_test_tbls',
            'TBLSPACE_TMP': 'default_test_tbls_tmp',
        },
    },
}

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

ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = False
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('zh-Hans', _('Simplified Chinese')),
]

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_ROOT = os.path.join(CONTENT_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets'),
]

LOCALE_PATHS = [
    os.path.join(CONTENT_DIR, 'locale')
]
