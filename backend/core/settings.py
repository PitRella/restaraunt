import os
from pathlib import Path
from datetime import timedelta
import environ
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env("SECRET_KEY", default=None) or get_random_secret_key()

DEBUG = env("DEBUG", False)
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'menu.apps.MenuConfig',
    'orders.apps.OrdersConfig',
    'user.apps.UserConfig',
    'comments.apps.CommentsConfig',
    # 3rd apps
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt.token_blacklist',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # local middleware
    'core.middlewares.APILoggingMiddleware',
]
ROOT_URLCONF = 'core.urls'
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

WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

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
SIMPLE_JWT = {
    'TOKEN_OBTAIN_SERIALIZER': 'user.serializers.CustomTokenObtainPairSerializer',
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Restaurant API',
    'DESCRIPTION': 'Документація API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_SETTINGS': {
        'persistAuthorization': True,
    },
    'COMPONENT_SPLIT_REQUEST': True,
    'AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
        }
    },
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
AUTH_USER_MODEL = 'user.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logs
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "django_server": {
            "format": "[%(asctime)s] \"%(message)s\"",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "api_requests": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "django_server_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/django_server.log",
            "formatter": "django_server",
        },
        "api_requests_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/api_requests.log",
            "formatter": "api_requests",
        },
    },
    "loggers": {
        "django.server": {
            "handlers": ["django_server_file"],
            "level": "INFO",
            "propagate": False,
        },
        "api_requests": {
            "handlers": ["api_requests_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
