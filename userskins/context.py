from userskins.models import SkinPreference
from django.conf import settings


def userskins(request):
    skin = settings.USERSKINS_DEFAULT
    if request.COOKIES.has_key("userskins"):
        skin = request.COOKIES["userskins"]
    if settings.USERSKINS_USE_COMPRESS_GROUPS:
        return {"userskins_skin": skin, "userskins_use_compress":True }
    else:
        skin_uri = u"%s%s" % (settings.MEDIA_URL, settings.USERSKINS_DETAILS[skin])
        return {"userskins_skin": skin_uri, "userskins_use_compress":False }
