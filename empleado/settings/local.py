from .base import *
import pymysql
pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'dc',
        'PASSWORD': 'dc',
        'PORT': '5432',
        'HOST': 'localhost'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',    'compressor.finders.CompressorFinder',)
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    '/static/',
]
MEDIA_URL = '/media/'
MEDIA_DIR = BASE_DIR / 'media'
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR.child('media')
