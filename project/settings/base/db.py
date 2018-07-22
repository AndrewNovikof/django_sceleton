import sys

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'assistant',
        'USER': 'assistant',
        'PASSWORD': 'kid58-yt4sn3g0qnpjzpiq6qeo8u4hilz',
        'HOST': 'db',
        'CONN_MAX_AGE': 900
    }
}
