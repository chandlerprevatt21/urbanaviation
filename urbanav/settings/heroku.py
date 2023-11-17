import environ
from .production import *

env = environ.Env(
    DEBUG=(bool, False)
)

DEBUG = False

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['www.urbanaviationgrp.com', 'urbanaviationgrp.com', 'urban-aviation-bb87a406e57a.herokuapp.com', 'urban-aviation.herokuapp.com', 'https://urban-aviation-bb87a406e57a.herokuapp.com']
