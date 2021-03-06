from django.utils.translation import ugettext_lazy as _

from oscar import get_core_apps, OSCAR_MAIN_TEMPLATE_DIR
from oscar.defaults import *

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(inskw5#o&cdm(bz0ahry+)fuk7$=9h$i&03m2&w(po*-wn+5m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

]

PROJECT_APPS = [
    'scaffold.apps.default',
    'scaffold.apps.catalogue',
    'scaffold.apps.dashboard.catalogue',
    'scaffold.apps.room',
]

HELPER_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',

    'versatileimagefield',
    'django_extensions',
    # 'compressor',
    'widget_tweaks',
]

OSCAR_APPS = ['oscar', 
              'oscar.apps.analytics', 
              'oscar.apps.checkout', 
              'oscar.apps.address', 
              'oscar.apps.shipping', 
              #'oscar.apps.catalogue', 
              'oscar.apps.catalogue.reviews', 
              'oscar.apps.partner', 
              'oscar.apps.basket', 
              'oscar.apps.payment', 
              'oscar.apps.offer', 
              'oscar.apps.order', 
              'oscar.apps.customer', 
              'oscar.apps.promotions', 
              'oscar.apps.search', 
              'oscar.apps.voucher', 
              'oscar.apps.wishlists', 
              'oscar.apps.dashboard', 
              'oscar.apps.dashboard.reports', 
              'oscar.apps.dashboard.users', 
              'oscar.apps.dashboard.orders', 
              'oscar.apps.dashboard.promotions', 
              # 'oscar.apps.dashboard.catalogue', 
              'oscar.apps.dashboard.offers', 
              'oscar.apps.dashboard.partners', 
              'oscar.apps.dashboard.pages', 
              'oscar.apps.dashboard.ranges', 
              'oscar.apps.dashboard.reviews', 
              'oscar.apps.dashboard.vouchers', 
              'oscar.apps.dashboard.communications', 
              'oscar.apps.dashboard.shipping', 

              'haystack', 
              'treebeard', 
              'sorl.thumbnail', 
              'django_tables2',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + HELPER_APPS + OSCAR_APPS  # + get_core_apps()

SITE_ID = 1

#
# Oscar settings
#
OSCAR_SHOP_NAME = 'ToSelf'
OSCAR_SHOP_TAGLINE = 'Moderne Zuhause'
OSCAR_ALLOW_ANON_REVIEWS = False
OSCAR_MODERATE_REVIEWS = True
OSCAR_EAGER_ALERTS = False

OSCAR_HIDDEN_FEATURES = [
    'reviews',
    'wishlists',
    'stock_alerts',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'scaffold.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'scaffold.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
]

OSCAR_DEFAULT_CURRENCY = 'EURO'
OSCAR_CURRENCY_LOCALE = 'de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        #print("Could not load local_settings")
        pass


