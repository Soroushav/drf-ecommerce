from .base import *
from .base import env

env.read_env(str(BASE_DIR.joinpath('.env', 'local', '.env')))
DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = ["*"]

