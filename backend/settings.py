"""
Django settings for metube project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: decouple this from settings
SECRET_KEY = '^sc7wh-girg@!l)adkjkc39k-kiiva*=!hay@6dr&el_4gqvb*'

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'djangobower',
    'compressor',
    'backend.blog',
    'backend.authentication',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'

TEMPLATE_DIRS = (
    #"backend/blog/templates",
    "frontend/",
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
    )

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "frontend"),
)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'backend.compressor_filters.PatchedSCSSCompiler'),
)
COMPRESS_CSS_FILTERS = (
    'backend.compressor_filters.CustomCssAbsoluteFilter',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'bower_components')

BOWER_INSTALLED_APPS = (
    'bootstrap-sass-official#3.3.1',
)

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the backend
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=backend',
]
