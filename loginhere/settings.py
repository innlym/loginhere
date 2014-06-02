
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'd9m=wuzic+owm9^^_17j2$g&kdy8t*7z^o8-ve^l6$^^768-$l'

DEBUG = False

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.1.1']

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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'loginhere',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}


LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Etc/GMT-8'

USE_I18N = True

USE_L10N = True

USE_TZ = True


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


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

EMAIL_HOST='smtp.exmail.qq.com'
EMAIL_HOST_USER='test@innlym.me'
EMAIL_HOST_PASSWORD='pw2014'
EMAIL_USE_TLS = False

SITE_NAME = 'Login Here'

