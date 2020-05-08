from .base import * 
DEBUG = False
# poner enlaces de las que crea que son confiables usualmente ponen la ip del servidor en el que funciona
ALLOWED_HOSTS = ['www.ejemplo.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}