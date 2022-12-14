import django_on_heroku
from decouple import config
from .base import *


# openssl rand -hex 32
SECRET_KEY = config('SECRET_KEY')


DEBUG = False

# web domain on heroku
ALLOWED_HOSTS = [
    'nawafaljumaiah-basic-blog.herokuapp.com',
    'nawafaljumaiah.blog.net'
]