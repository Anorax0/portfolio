# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'bzx+b@*7_2c5ew58%-8(3qjhgx=5+y7v472u$dk#3yq&*71r37'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'postgres',
        'PASSWORD': 'justword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# DARKSKY_API_KEY = '89aeb1016e0e5068c14f91c54687d28c'
