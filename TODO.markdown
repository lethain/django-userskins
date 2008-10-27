
## TODO TASKS

1.  Can we create a flexible general purpose view to
    handle the process of assigning users a skin.
    Essentially that involves a) setting a cookie in
    the response, and b) create a SkinPreference instance
    for the user and skin.

2.  Update README to discuss handling skin selection,
    and discuss the technical details behind how skins
    preference is remembered (stored in a cookie, but
    if the cookie is deleted will refresh the cookie
    from the database if the user has established a
    preference).

3.  Add an option to disable hitting the database if
    a user is missing the cookie. (Only use cookies for
    skin preference persistence.)

4.  Test that the integration with django-compress
    actually works (pretty sure it does ;).