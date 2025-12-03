from .base import *
import os

DEBUG = False

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", 'set-a-secret-key-please')

if SECRET_KEY == 'set-a-secret-key-please':
    print('If you see this outside of a docker container build, SOMETHING IS WRONG. Set a secret key!!!')

else:  # yes, this is terrible, but it makes docker build work.
    ALLOWED_HOSTS = [host for host in os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')]
    CSRF_TRUSTED_ORIGINS = ['https://' + host for host in ALLOWED_HOSTS]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ["DB_HOST"],
            "NAME": os.environ["DB_NAME"],
            "USER": os.environ["DB_USER"],
            "PASSWORD": os.environ["DB_PASSWORD"],
            "OPTIONS": {
                "client_encoding": "UTF8",
            },
        }
    }

try:
    from .local import *
except ImportError:
    pass
