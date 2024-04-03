pip install tensorflow
pip install sklearn

/config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatdb',
        'USER': 'root',
        'PASSWORD': 'intra165',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
