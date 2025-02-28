"""
Django settings for fater project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import locale
locale.setlocale(locale.LC_ALL, "fa_IR")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ts(&i-rv2))hcv*$vq_$he-6mcv588a1!)ako-#$=al4p_i1*e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ip='http://127.0.0.1:8000'
# ALLOWED_HOSTS = ['127.0.0.1']

#server
ip='http://194.135.90.60'
ALLOWED_HOSTS = ['194.135.90.60']


# Application definition

INSTALLED_APPS = [
    'django_jalali',
    'jet.dashboard',
    'jet',
    'ckeditor_uploader',
    'mesineapp',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',


]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
JET_SIDE_MENU_COMPACT = True
JET_DEFAULT_THEME = 'light-gray'
# JET_CHANGE_FORM_SIBLING_LINKS = True
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secrets.json')

JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'

JET_SIDE_MENU_ITEMS = [ # A list of application or custom item dicts
    {'label': ('مسینه'), 'app_label': 'core', 'items': [
        {'label': ('ارزش های پیشنهادی'), 'url':  ip + '/back_end/admin/mesineapp/%D8%A7%D8%B1%D8%B2%D8%B4_%D9%87%D8%A7%DB%8C_%D9%BE%DB%8C%D8%B4%D9%86%D9%87%D8%A7%D8%AF%DB%8C/'},
        {'label': ('بنر ها'), 'url':  ip + '/back_end/admin/mesineapp/%D8%A8%D9%86%D8%B1/' },
        {'label': ('تماس با ما'), 'url':  ip + '/back_end/admin/mesineapp/%D8%AA%D9%85%D8%A7%D8%B3_%D8%A8%D8%A7_%D9%85%D8%A7/' },
        {'label': ('خبر ها'), 'url':  ip + '/back_end/admin/mesineapp/%D8%AE%D8%A8%D8%B1/' },
        {'label': ('درباره ما'), 'url':  ip + '/back_end/admin/mesineapp/%D8%AF%D8%B1%D8%A8%D8%A7%D8%B1%D9%87_%D9%85%D8%A7/' },
        {'label': ('سرویس ها'), 'url':  ip + '/back_end/admin/mesineapp/%D8%B3%D8%B1%D9%88%DB%8C%D8%B3/' },
        {'label': ('شبکه اجتماعی'), 'url':  ip + '/back_end/admin/mesineapp/%D8%B4%D8%A8%DA%A9%D9%87_%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%DB%8C/' },
        {'label': ('لوگو'), 'url':  ip + '/back_end/admin/mesineapp/%D9%84%D9%88%DA%AF%D9%88/' },
        {'label': ('منوی غذا'), 'url':  ip + '/back_end/admin/mesineapp/%D9%85%D9%86%D9%88%DB%8C_%D8%BA%D8%B0%D8%A7/' },
        {'label': ('منوی محبوب رستوران'), 'url':  ip + '/back_end/admin/mesineapp/%D9%85%D9%86%D9%88%DB%8C_%D9%85%D8%AD%D8%A8%D9%88%D8%A8_%D8%B1%D8%B3%D8%AA%D9%88%D8%B1%D8%A7%D9%86/' },

    ]},
    {'label': ('مدیریت'), 'items': [
        {'name': 'auth.user'},
        {'name': 'auth.group'},
    ]},
]

# ROOT_URLCONF = 'fater.urls'


#server
ROOT_URLCONF = 'mesineh.urls'


TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#server
WSGI_APPLICATION = 'mesineh.wsgi.application'




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
#     }
# }

#server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mesinedatabase',
        'USER': 'mesineuser',
        'PASSWORD': 'MessinehOriginalPassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}






# WSGI_APPLICATION = 'fater.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'Mediastorage/'
CKEDITOR_IMAGE_BACKEND = "pillow"

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': None,
#     },
# }

###################################
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 200,
        'toolbar_Custom': [
            [ 'Preview','spellchecker''-', 'Templates' ,'Undo', 'Redo' , 'Scayt' ,],
            ['Styles', 'Format', 'Font', 'FontSize' , 'Bold', 'Italic', 'Underline', 'Strike', '-',],
            ['Link', 'Unlink', 'Anchor'],
            [ 'NumberedList', 'BulletedList', '-''JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',] ,
            ['Link', 'Unlink',],
            ['Document', 'Mode', 'Doctools' ],
            ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar',],
            ['TextColor', 'BGColor'],
            ['Source'],
        ],
        # 'extraPlugins': 'easyimage',
        # 'removePlugins': 'image',
    },
    'special': {
        'toolbar': 'Special',
        'toolbar_Special': [
            ['Bold'],
        ],
    }
}



JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [ # prefix address is 'admin/'
            'js/django_jalali.min.js',
            # or
            # 'jquery.ui.datepicker.jalali/scripts/jquery-1.10.2.min.js',
            # 'jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "messineh.resturant@gmail.com"
EMAIL_HOST_PASSWORD = "Messi..Neh20"
# APPEND_SLASH = False

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = False

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static_back_end/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_back_end')

STATICFILES_DIRS = [
os.path.join(BASE_DIR, "static_back_end"),
]

MEDIA_URL = '/Back_end_Media/'
MEDIA_ROOT = 'Back_end_Media/'
