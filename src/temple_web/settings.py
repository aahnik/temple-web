"""
Django settings for temple_web project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from .myconfig import MyDjangoSettings as MyDjS

import logging
import os

log = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = MyDjS.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = MyDjS.DEBUG

MY_LOCAL_IP = "192.168.1.12"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".ngrok-free.app",
    "0.0.0.0",
]
if MyDjS.DEBUG:
    ALLOWED_HOSTS += [MY_LOCAL_IP]
if MyDjS.MORE_ALLOWED_HOSTS:
    ALLOWED_HOSTS += MyDjS.MORE_ALLOWED_HOSTS
# print(ALLOWED_HOSTS)
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://*.ngrok-free.app/",
]

if MyDjS.PROD:
    ALLOWED_HOSTS.append(f".{MyDjS.PROD_DOMAIN}")
    CSRF_TRUSTED_ORIGINS.append(f"https://*.{MyDjS.PROD_DOMAIN}")


AUTH_USER_MODEL = "users.TempleWebUser"

INSTALLED_APPS = [
    # core django apps
    # "django.contrib.admin",
    "temple_web.apps.TempleWebAdminConfig",
    # use a custom admin site instance
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party apps
    "solo.apps.SoloAppConfig",
    # our custom apps
    "home.apps.HomeConfig",
    "donations.apps.DonationsConfig",
    # "donations.apps.OnlinePujaConfig",
    "activities.apps.ActivitiesConfig",
    "accounts.apps.AccountsConfig",
    "tester.apps.TesterConfig",
    "users.apps.UsersConfig",
    "haps",
    # more third party apps
    # recommended to be placed at last
    "django_cleanup.apps.CleanupConfig",
    "crispy_forms",
    "crispy_tailwind",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "temple_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "home.context_processors.site_ctx",
            ],
        },
    },
]

WSGI_APPLICATION = "temple_web.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
# STATIC_ROOT = ""
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

FILES_BASE = Path(MyDjS.PROD_FILES_ROOT) / MyDjS.PROD_DOMAIN

if MyDjS.PROD:
    STATIC_ROOT = FILES_BASE / "static"

else:
    STATIC_ROOT = BASE_DIR.parent / "local-cdn" / "static"

MEDIA_URL = "/media/"

if MyDjS.PROD:
    MEDIA_ROOT = FILES_BASE / "media"
else:
    MEDIA_ROOT = BASE_DIR.parent / "local-cdn" / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"
