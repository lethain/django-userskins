
### CONCEPT

The purpose of django-userskins is to allow Django apps
to allow users to select from a variety of provided skins
to customize how a site looks for them. Essentially, to
provide the functionality exposed in Twitter's recent
update where users can choose from a handful of different
appearances for how Twitter appears when they visit the
site.


# IMPLEMENTATION

Django-userskins' implementation is designed to minimize
additional hits on the database, but to allow the skin
preference to persist across cleanings of the cookie cache.

The implementation is split into a template processing context,
a template tag, and a middleware.

#### userskins.context.userskins

The behavior of the custom template processing context
is:

1.  Check if the user has a cookie named ``userskins``.
    If so, use its value to select the skin.

2.  Otherwise use the default skin.

#### userskins.middleware.UserskinsMiddleware

The behavior of the middleware is to examine all
HttpResponse objects and:

1.  If the HttpResponse object has a cookie named
    ``userskins``, do nothing.

2.  If the response does not have a cookie named ``userskins``,
    then if the user is anonymous give it a ``userskins`` cookie
    for the default skin.

    If the user is authenticated, then attempt to retrieve a
    ``userskins.SkinPreference`` object with the logged in user
    as the value of its ``user`` foreign key.

    (Note that this is the only hit on the database that the
    userskins app will cause. Meaning, it will only hit the
    database for logged in users who don't already have a
    userskins cookie. When it does hit the database, it will
    set a cookie for the user, so it should only be necessary
    to hit the database once each time a user cleans their
    cookie cache.)

    Set the value of the ``userskins`` cookie to the value stored
    in the ``SkinPreference`` object if one exists, otherwise set
    it to the default skin.

#### userskins.templatetags.userskins

The ``userskins`` template tag library contains one template
tag, ``userskin``, which takes no arguments and handles outputing
the correct CSS include or (if you have the correct settings enabled)
django-compress group.


# SETUP

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

