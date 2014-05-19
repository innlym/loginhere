"""
Django settings for loginhere project.

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
SECRET_KEY = 'd9m=wuzic+owm9^^_17j2$g&kdy8t*7z^o8-ve^l6$^^768-$l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'oauth2_provider',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'loginhere.urls'

WSGI_APPLICATION = 'loginhere.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

#CORS_URLS_REGEX = '^.*$'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'loginhere',
        'USER': 'loginhere',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Etc/GMT-8'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'
STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT,'css')),
    ("js", os.path.join(STATIC_ROOT,'js')),
    ("img", os.path.join(STATIC_ROOT,'img')),
    ("fonts", os.path.join(STATIC_ROOT, 'fonts')),
)


# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR + '/media'

TEMPLATE_DIRS = (
    BASE_DIR + '/templates',
)


AUTH_USER_MODEL = 'accounts.HereUser'

# email config
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='innlym@gmail.com'
EMAIL_HOST_PASSWORD='idwnspw2gg'
EMAIL_USE_TLS = True

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

EMAIL_HOST='smtp.exmail.qq.com'
EMAIL_HOST_USER='test@innlym.me'
EMAIL_HOST_PASSWORD='pw2014'
EMAIL_USE_TLS = False

SITE_NAME = 'Login Here'
