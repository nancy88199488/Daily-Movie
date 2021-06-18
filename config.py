
# import os

# class Config:

#     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
#     MOVIE_API_KEY = os.environ.get('0b2773cd1fc8f86252f707f5c9b61dd1')
#     SECRET_KEY = os.environ.get('SECRET_KEY')

#     SQLALCHEMY_TRACK_MODIFICATIONS=True 
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nancy@localhost/movie'
#     UPLOADED_PHOTOS_DEST ='app/static/photos' #specifies the destination where we store our IMAGES

#     #  email configurations
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

#  # simple mde  configurations
#     SIMPLEMDE_JS_IIFE = True
#     SIMPLEMDE_USE_CDN = True

# class ProdConfig(Config):
#      SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# class ProdConfig(Config):
#   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
#   if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#     SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)


# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nancy@localhost/movie'
#     DEBUG = True

# class TestConfig(Config):
#   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nancy@localhost/movie_test'

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig,
# 'test':TestConfig
# }

import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    GENRES_URL ='https://api.themoviedb.org/3/genre/movie/list?api_key={}'
    TRAILERS_URL = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}&language=en-US'
    GENRE_MOVIES_URL = 'https://api.themoviedb.org/3/discover/movie?api_key={}&with_genres={}'



    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nancy@localhost/movie'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}