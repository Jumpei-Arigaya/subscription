# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l5q_r(!&j&2dcxs6=1kr8b=439=u55$zswl=80y^1+jdz3+%!h'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sub-db',
        'USER': 'sub-db',
        'PASSWORD': 'sub-db',
        'HOST': 'db',
        'PORT': '3306',
    }
}
