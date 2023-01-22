# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-umi*ku-pyri$9z%!n6!eag3-h(7%y2$l#_uq+27epxzl4chr^3'




# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'HERO_VILLANS' / 'mysql',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
