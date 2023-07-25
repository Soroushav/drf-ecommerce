from .base import *
from .base import env

env.read_env(str(BASE_DIR.joinpath('.env', 'local', '.env')))
DEBUG = env.bool("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': env("DB_ENGINE"),
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': 5432
    }
}