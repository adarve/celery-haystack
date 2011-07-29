from os import path

here = path.dirname(__file__)

INSTALLED_APPS = [
    'haystack',
    'djcelery',
    'celery_haystack',
    'notes',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': path.join(here, 'whoosh_index'),
    }
}

BROKER_TRANSPORT = "memory"
CELERY_IGNORE_RESULT = True
CELERYD_LOG_LEVEL = "DEBUG"
CELERY_DEFAULT_QUEUE = "celery-haystack"
