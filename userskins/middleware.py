from django.conf import settings
from userskins.models import SkinPreference


class UserskinsMiddleware(object):
    def process_response(self, request, response):
        if not request.COOKIES.has_key("userskins"):
            skin = settings.USERSKINS_DEFAULT
            if request.user.is_authenticated():
                try:
                    skin = SkinPreference.objects.get(user=request.user).skin
                except SkinPreference.ObjectDoesNotExist:
                    pass
            response.set_cookie("userskins", skin)
        return response
