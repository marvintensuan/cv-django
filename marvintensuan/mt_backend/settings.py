# Import the original settings from each template
from .basesettings import *

try:
    from .local import *
except ImportError:
    pass

# Pulling django-environ settings file, stored in Secret Manager
import environ
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file = os.path.join(BASE_DIR,  ".env")

SETTINGS_NAME = "application_settings"

if not os.path.isfile('.env'):
    import google.auth
    from google.cloud import secretmanager_v1beta1 as sm

    _, project = google.auth.default()

    if project:
        client = sm.SecretManagerServiceClient()
        path = client.secret_version_path(project, SETTINGS_NAME, "latest")
        payload = client.access_secret_version(path).payload.data.decode("UTF-8")

        with open(env_file, "w") as f:
            f.write(payload)

env = environ.Env()
env.read_env(env_file)

# Setting this value from django-environ
SECRET_KEY = env("SECRET_KEY")

# Could be more explicitly set (see "Improvements")
ALLOWED_HOSTS = ["*"]

# Default false. True allows default landing pages to be visible
DEBUG = env("DEBUG")

# Setting this value from django-environ
DATABASES = {"default": env.db()}


INSTALLED_APPS += ["storages"] # for django-storages
if "mt_backend" not in INSTALLED_APPS:
   INSTALLED_APPS += ["mt_backend"] # for custom data migration

# Define static storage via django-storages[google]
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
STATICFILES_DIRS = []
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_DEFAULT_ACL = "publicRead"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    BASE_DIR + 'templates',
                    BASE_DIR + 'mt_backend/templates',
                    '/mt_backend/templates',
                    '/templates',
                ],
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
