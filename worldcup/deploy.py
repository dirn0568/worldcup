
from .settings import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# reading .env file
environ.Env.read_env(
    env_file= os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# 마리아db를 사용해도 ENGINE에 mysql이 나옴(mysql 유로프로그램에서 나온 무료시스템이여서)
# 마리아db, mysql 모두 포트는 3306
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django2',
        'USER': 'django2',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'HOST': 'mariadb2',
        'PORT': '3306',
    }
}

