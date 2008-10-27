from django.conf import settings
from userskins.models import SkinPreference
import django

class UserskinsMiddleware(object):
    def __init__(self):
        never_use_database = getattr(settings,"USERSKINS_NEVER_ACCESS_DATABASE", False)
        if never_use_database:
            raise django.core.exceptions.MiddlewareNotUsed

    def process_response(self, request, response):
        print "wee"
        if not request.COOKIES.has_key("userskins"):
            skin = settings.USERSKINS_DEFAULT
            if request.user.is_authenticated():
                try:
                    skin = SkinPreference.objects.get(user=request.user).skin
                except SkinPreference.ObjectDoesNotExist:
                    pass
            response.set_cookie("userskins", skin)
        return response
