# coding: utf-8
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TODO: split dev & prod settings
SECRET_KEY = '+g%2gck725lg6ilah5h)obimt3*_x9r7q#0&(&9ak7s&tnbg)s'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', ]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # system
    'rest_framework',

    # domain
    'prqueue.rest',
    'prqueue.developers',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'prqueue.urls'

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

WSGI_APPLICATION = 'prqueue.wsgi.application'

# local
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# static etc
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + STATIC_URL

# rest settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# celery settings
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

# TODO: read from prod settings
# MAIL PROCESSOR config
MAILPROCESSOR_LOGIN = ''
MAILPROCESSOR_PASSWORD = ''
MAILPROCESSOR_SMTP_HOST = ''
MAILPROCESSOR_SUBJECT = '[Hero of a day] Who is on duty today?'
MAILPROCESSOR_FROM = ''
MAILPROCESSOR_RECEIVER_DEBUG = ''