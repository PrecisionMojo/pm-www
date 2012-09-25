"""Base settings available to all environments."""

# Based on https://github.com/rdegges/django-skel and
# https://github.com/cyberdelia/django-heroku-template.

import os
import sys

## Path configuration
# Absolute path to our project directory.
# NOTE: Use dirname() twice as the settings file is two levels deep.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create an absolute path from a path relative to the project root.
project_path = lambda path: os.path.normpath(os.path.join(PROJECT_ROOT, path))

# Absolute path to our site directory.
SITE_ROOT = os.path.dirname(PROJECT_ROOT)

# Name of the site.
SITE_NAME = os.path.basename(PROJECT_ROOT)

# Add our project root to the pythonpath so that we can refer to project
# modules without having to use the project's name.
sys.path.append(PROJECT_ROOT)


## Debug configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


## Admin and manager configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


## Timezone and localization configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Phoenix'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


## Media configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = project_path('media/')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


## Static files configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = project_path('static/')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-dirs
STATICFILES_DIRS = (
    project_path('assets/'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


## Secret key configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = '4=py*2g1gl=cgjqcb4v*gr^&amp;5nxt2@d%b+!#l(2eeb#sa_0yxq'


## Template configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
# TODO: Use another setting instead of DEBUG.
if not DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
else:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    project_path('templates/')
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
# NOTE: All except the last are defaults.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)


## Middleware configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


## URL configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME


## WSGI configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME


## Installed app configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/humanize/
    'django.contrib.humanize',

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/
    'django.contrib.admin',
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/admindocs/
    'django.contrib.admindocs',
)


## Logging configuration
# NOTE: Don't filter HTTP 500 error emails in not DEBUG environments (the
# default configuration does this).
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}