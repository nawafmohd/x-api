from decouple import config
from .base import *

# openssl rand -hex 32
SECRET_KEY = config('SECRET_KEY')


DEBUG = True


ALLOWED_HOSTS = [
    'http://127.0.0.1:3000/',
    'http://localhost:3000/',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1',
    'http://localhost',
    '127.0.0.1',
    'localhost'
]