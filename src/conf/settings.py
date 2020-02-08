import os

from rhea import Rhea

rhea_config = Rhea.read_configs(os.environ)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = rhea_config.get_string('SECRET_KEY')
DEBUG = rhea_config.get_boolean('DEBUG', is_optional=True, default=False)
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'cities',
    'api',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'conf.urls'
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
WSGI_APPLICATION = 'conf.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': rhea_config.get_string('POSTGRES_DB'),
        'USER': rhea_config.get_string('POSTGRES_USER'),
        'PASSWORD': rhea_config.get_string('POSTGRES_PASSWORD'),
        'HOST': rhea_config.get_string('POSTGRES_HOST'),
        'PORT': rhea_config.get_string('POSTGRES_PORT'),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
CITIES_DATA_DIR = rhea_config.get_string('CITIES_DATA_DIR', default='/tmp/', is_optional=True)
CITIES_FILES = {
    'city': {
        'filenames': ['RU.zip', ],
        'urls':      ['http://download.geonames.org/export/dump/'+'{filename}']
    },
}
CITIES_LOCALES = ['ru', ]
CITIES_POSTAL_CODES = ['RU', ]
