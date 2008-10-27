
### SETUP

1.  Add ``django-userskins.userskins`` to your Python path.

2.  Add ``userskins`` to your applications ``INSTALLED_APPS``
    setting in settings.py.

3.  Add the ``userskins.context.userskins`` template context
    processor in ``settings.py`` (note that this will be a
    new setting in your settings.py file, by default it is
    not shown):

        TEMPLATE_CONTEXT_PROCESSORS = (
            "django.core.context_processors.auth",
            "django.core.context_processors.debug",
            "django.core.context_processors.i18n",
            "django.core.context_processors.media",
            "userskins.context.userskins",
            )

4.  Add the ``userskins.middleware.UserskinsMiddleware``
    middleware to your project's middleware.

        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'userskins.middleware.UserskinsMiddleware',
        )

    The position of the ``UserskinsMiddleware`` shouldn't be
    signifigant.

5.  Establish values for the ``USERSKINS_DEFAULT``, ``USERSKINS_DETAILS``
    and ``USERSKINS_USE_COMPRESS_GROUPS_INSTEAD`` values in your
    settings.py file.

        USERSKINS_DEFAULT = "light"
        USERSKINS_DETAILS = {
            'light':'light.css',
            'dark':'dark.css',
        }
        USERSKINS_USE_COMPRESS_GROUPS = False

    ``USERSKINS_USE_COMPRESS_GROUPS`` is to support integration
    with the django-compress project. In that case, the values of keys
    in ``USERSKINS_DETAILS`` are ignored, and the keys themselves are
    passed to the django-compress template tags as names of compressed
    css groups.

    It is highly recommended to use django-userskins along with
    django-compress, as it will allow you to provide users with
    selectable skins without increasing the median bandwith per
    request or the median number of http requests per page.

6.  Now modify your base template (or wherever you want to use skins)
    to resemble this code:

        {% load userskins %}
        <html><head>
        <title> Some title </title>
        {% userskin %}
        </head>
        <body>
        {% block content %}{% endblock %}
        </body>
        </html>

    And you're done.

