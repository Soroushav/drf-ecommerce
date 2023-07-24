from .base import *
from .base import env

env.read_env(str(BASE_DIR.joinpath('.env', 'local', '.env')))
DEBUG = env.bool("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

