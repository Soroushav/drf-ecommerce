from .base import *

env.read_env(str(BASE_DIR.joinpath('.env', 'production', '.env')))
DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = ['*']