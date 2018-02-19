"""
Django settings for Appraise project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import logging
from logging.handlers import RotatingFileHandler

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Try to load local settings, otherwise use defaults.
try:
    # pylint: disable=W0611
    from Appraise.local_settings import DEBUG, ADMINS, MANAGERS, DATABASES, \
      SECRET_KEY, ALLOWED_HOSTS, SECURE_CONTENT_TYPE_NOSNIFF, \
      SECURE_BROWSER_XSS_FILTER, SESSION_COOKIE_SECURE, \
      CSRF_COOKIE_SECURE, X_FRAME_OPTIONS, WSGI_APPLICATION

except ImportError:
    DEBUG = True

    ADMINS = ()
    MANAGERS = ADMINS

    # pylint: disable=C0330
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'development.db'),
      }
    }

    SECRET_KEY = 'j^g&cs_-8-%gwx**xmq64pcm6o2c3ovrxy&%9n@ez#b=qi!uc%'
    ALLOWED_HOSTS = ['127.0.0.1']

    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    X_FRAME_OPTIONS = 'DENY'

    WSGI_APPLICATION = 'Appraise.wsgi.application'

# Logging settings for this Django project.
LOG_LEVEL = logging.DEBUG
LOG_FILENAME = os.path.join(BASE_DIR, 'appraise.log')
LOG_FORMAT = "[%(asctime)s] %(name)s::%(levelname)s %(message)s"
LOG_DATE = "%m/%d/%Y @ %H:%M:%S"
LOG_FORMATTER = logging.Formatter(LOG_FORMAT, LOG_DATE)

# pylint: disable=C0330
LOG_HANDLER = RotatingFileHandler(filename=LOG_FILENAME, mode="a",
  maxBytes=50*1024*1024, backupCount=5, encoding="utf-8")
LOG_HANDLER.setLevel(level=LOG_LEVEL)
LOG_HANDLER.setFormatter(LOG_FORMATTER)

LOGIN_URL = '/dashboard/sign-in/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Dashboard',
    'EvalView',
    'EvalData',
    'Campaign',
]

if DEBUG:
    try:
        # pylint: disable=W0611
        import debug_toolbar
        INSTALLED_APPS.append('debug_toolbar')

    except ImportError:
        pass

MIDDLEWARE = []
if DEBUG:
    if 'debug_toolbar' in INSTALLED_APPS:
        MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

MIDDLEWARE.extend([
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
])

ROOT_URLCONF = 'Appraise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Base context for all views.
BASE_CONTEXT = {
  'commit_tag': '#wmt18dev',
  'title': 'Appraise evaluation system',
  'static_url': STATIC_URL,
}

if DEBUG:
    INTERNAL_IPS = [
      '127.0.0.1'
    ]
