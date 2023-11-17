import environ
from .production import *

env = environ.Env(
    DEBUG=(bool, False)
)

DEBUG = False

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['www.urbanaviationgrp.com', 'urbanaviationgrp.com', 'elift.herokuapp.com']
