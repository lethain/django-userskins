from django.conf.urls.defaults import *
from django.template import RequestContext
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def dark(request):
    hrr = HttpResponseRedirect("/")
    hrr.set_cookie("userskins", "dark")
    return hrr

def light(request):
    hrr = HttpResponseRedirect("/")
    hrr.set_cookie("userskins", "light")
    return hrr

urlpatterns = patterns(
    '',
    (r'^$','django.views.generic.simple.direct_to_template',
     {'template':'dev_index.html'}),
    (r'^dark/$',dark),
    (r'^light/$',light),
)
