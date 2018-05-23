## Django Rest Framework Discovery

[![Build Status](https://travis-ci.org/ztroop/django-rest-framework-discovery.svg?branch=master)](https://travis-ci.org/ztroop/django-rest-framework-discovery)
[![PyPI version](https://badge.fury.io/py/djangorestframework-discovery.svg)](https://badge.fury.io/py/djangorestframework-discovery)

Discovery allows you to create an API from an existing database with little to no effort. This project is based on Shabda Raaj's [Bookrest][1]. You can then leverage the capabilties of the Django Rest Framework to apply [filtering][2], [pagination][3] and [documentation][4] generation.

[1]: https://github.com/agiliq/bookrest
[2]: https://django-rest-framework.org/api-guide/filtering/
[3]: https://django-rest-framework.org/api-guide/pagination/
[4]: https://django-rest-framework.org/topics/documenting-your-api/

### Requirements

For successful generation, you need to have a primary key present in the table. Otherwise, it will be silently ignored.

### Installation

```bash
pip install djangorestframework-discovery
```

In your `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    "rest_framework",
    "rest_framework_discovery",
]
```

Add a variable to your `settings.py` named `DISCOVERY_ALIAS_NAME`. You can use any value, but `discovery` is recommended. You will use that to define the database you would like to use for viewset generation.

```python
DISCOVERY_ALIAS_NAME = 'discovery'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'discovery': {
        'NAME': 'YOUR_DB_NAME',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'YOUR_DB_USER',
        'PASSWORD': 'YOUR_DB_PASSWORD',
        'HOST': 'YOUR_DB_HOST',
        'PORT': 'YOUR_DB_PORT',
    },
}
```

Add the generated patterns to the rest of your application by modifying the `urls.py`.

```python
urlpatterns = [
    # ...
    url(r'^api/discovery/', include('rest_framework_discovery.urls')),
]
```

### Testing

You can run through the testing suite by running `runtests.py` or `tox`.

### Configuration

You can configure the following in `settings.py`:
- `DISCOVERY_ALIAS_NAME`: (required) The database profile name to use with discovery.
- `DISCOVERY_READ_ONLY`: (optional) `True` or `False`, whether or not the viewsets should be read-only.
- `DISCOVERY_INCLUDE`: (optional) A list of tables that you would like to *only* include.
- `DISCOVERY_EXCLUDE`: (optional) A list of tables that you would like to ignore.
