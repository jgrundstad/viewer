# Variant Report Viewer
Web application to load, annotate, parse, search, and display annotated Variant and Mutation data

---

## Requirements

###Debian/Ubuntu:

* xvfb - required for driving headless instance of Firefox for web-scraping 
* Firefox

###Python:

* Django==1.7.4
* EasyProcess==0.1.9
* PyVirtualDisplay==0.1.5
* argparse==1.2.1
* beautifulsoup4==4.3.2
* django-admin-bootstrapped==2.3.2
* django-crontab==0.6.0
* django-extensions==1.5.2
* django-password-reset==0.7
* django-uuidfield==0.5.0
* ipython==3.1.0
* mysqlclient==1.3.5
* pydot==1.0.2
* pygraphviz==1.2
* pyparsing==1.5.7
* pytz==2014.10
* requests==2.6.0
* selenium==2.47.0
* simplejson==3.6.5
* six==1.9.0
* tablib==0.10.0
* uWSGI==2.0.10
* wsgiref==0.1.2

---

## Edits to Site (root) settings files:
Place the ```viewer``` directory into your new or pre-existing site directory, then make the following updates and additions.

### settings.py
```python
# Application definition
INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viewer',
    'django_extensions',
    'django_crontab',
    'password_reset',
)

# EMAIL and SMTP settings
# Only needed for production
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.someservice.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'joe@email.add'
EMAIL_HOST_PASSWORD = email_host_password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# this can be done in debug mode with a simple sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': BASE_DIR + '/igsb_report_viewer/my.cnf',
        },
    }
}

# Cronjobs, only needed in production
CRONJOBS = [
        ('10 2 * * *',
            'viewer.links_out.cron.gather_md_anderson')
]

# Static file and media links
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/viewer/files/'
MEDIA_URL = '/viewer/files/'
LINKS_OUT = BASE_DIR + '/viewer/links_out/'
LOGIN_URL = '/viewer/login/'
```

### my.cnf (as referenced in the ```# Database``` section above)
Create the mysql database with the same parameters used in the ```my.cnf``` file:
```python
[client]
database = report_viewer
user = dbusername
password = dbpassword
host = dbhost
default-character-set = utf8
```
When the database server is running, and the database has been created, be sure to create the django superuser:
```python
python manage.py createsuperuser
```


### urls.py
```python
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^viewer/', include('viewer.urls')),
                       url(r'^password_reset/', include('password_reset.urls')),
                      )
```

## Create 'project_user' group through the django admin interface
Under the ```groups``` section, select ```"Add Group"```, then apply these permissions:
* Caller, Genome
  * Add 
* Project
  * Add
  * Change
* Study, Sample, Bnid, Report, Variant
  * Add
  * Change
  * Delete

Every user that registers must be added to the project_user group to be able to use the application.

