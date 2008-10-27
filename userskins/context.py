from userskins.models import SkinPreference
from django.conf import settings


def userskins(request):
    skin = settings.USERSKINS_DEFAULT
    if request.COOKIES.has_key("userskins"):
        skin = request.COOKIES["userskins"]
    elif request.user.is_authenticated():
        try:
            skin = SkinPreference.objects.get(user=request.user).skin
        except SkinPreference.ObjectDoesNotExist:
            pass
        # note that this doesn't work. I'll have to
        # use a response middleware of some sort to
        # acchieve the desired effect
        request.COOKIES["userskins"] = skin

    if settings.USERSKINS_USE_COMPRESS_GROUPS:
        return {"userskins_skin": skin, "userskins_use_compress":True }
    else:
        skin_uri = u"%s%s" % (settings.MEDIA_URL, settings.USERSKINS_DETAILS[skin])
        return {"userskins_skin": skin_uri, "userskins_use_compress":False }
