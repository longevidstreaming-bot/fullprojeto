import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_HOST = os.environ.get("FRONTEND_HOST", "http://localhost:8000")
PORTAL_NAME = "MediaCMS"
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

SECRET_KEY = "dev-only-key-change-in-prod"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "mediacms-local",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.db"

BROKER_URL = "memory://"
CELERY_RESULT_BACKEND = "cache+memory://"
CELERY_TASK_ALWAYS_EAGER = True

DO_NOT_TRANSCODE_VIDEO = True

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "static_collected")

INSTALLED_APPS = [
    "admin_customizations",
    "django.contrib.auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.sites",
    "rest_framework",
    "rest_framework.authtoken",
    "imagekit",
    "files.apps.FilesConfig",
    "users.apps.UsersConfig",
    "actions.apps.ActionsConfig",
    "rbac.apps.RbacConfig",
    "identity_providers.apps.IdentityProvidersConfig",
    "mptt",
    "crispy_forms",
    "crispy_bootstrap5",
    "uploader.apps.UploaderConfig",
    "djcelery_email",
    "drf_yasg",
    "tinymce",
]
