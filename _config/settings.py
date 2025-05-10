import os
from pathlib import Path

from _config.unfold_config import UNFOLD

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Импорт функции для загрузки переменных окружения из файла .env
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Секретный ключ для безопасности проекта
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "unfold", 
    "unfold.contrib.filters", 
    "unfold.contrib.forms", 
    "unfold.contrib.inlines", 
    "unfold.contrib.import_export", 
    "unfold.contrib.guardian",  
    "unfold.contrib.simple_history",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tailwind', 
    'tailwind_config',
    'django_browser_reload',

    'addresses',
    'appointments',
    'contracts',
    'dental',
    'employees',
    'patients',
    'services',
    'pages'
]

TAILWIND_APP_NAME = 'tailwind_config'
INTERNAL_IPS = ["127.0.0.1"]
NPM_BIN_PATH = 'npm.cmd'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


ROOT_URLCONF = '_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '_config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Папка для собранных статических файлов (для продакшена)
STATIC_URL = 'static/' 
STATIC_ROOT = BASE_DIR / 'static'

# Дополнительные папки со статическими файлами (для разработки)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_dev'),
]

# Настройки медиафайлов (загружаемые пользователями файлы)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
