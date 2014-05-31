# Django settings for arkansassymphony project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Brandon Dorris', 'admin@arkansassymphony.org'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'arkansassymphony',                      # Or path to database file if using sqlite3.
        'USER': 'webadmin',                      # Not used with sqlite3.
        'PASSWORD': 'asomusic',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

STATIC_URL = '/static/'

STATIC_ROOT = '/arkansassymphony/static/'

STATICFILES_DIRS = (
   ' /arkansassymphony/static/registration/'

)
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/arkansassymphony/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ho^iecr0$o4zh_@fh4#l(zniexuw+@g3&d1f(9_n0k!z!#4f-7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'arkansassymphony.urls'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/arkansassymphony/templates/',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'musicians@arkansassymphony.org'
EMAIL_HOST_PASSWORD = 'aso123music'
EMAIL_PORT = 587


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'arkansassymphony.concerts',
    'arkansassymphony.people',
    'arkansassymphony.sponsors',
    'arkansassymphony.multimedia',
    'arkansassymphony.comments',
    'arkansassymphony.youthcalendar',
    'arkansassymphony.jobs',
    'arkansassymphony.staff_board',
    'arkansassymphony.musicians',
    'arkansassymphony.galleries',
    'arkansassymphony.designerhouse',
    'arkansassymphony.checkin',
    'arkansassymphony.donation',
    'arkansassymphony.rsvp',
    'arkansassymphony.venue',
    'arkansassymphony.registration',
    'arkansassymphony.teachers',
)
