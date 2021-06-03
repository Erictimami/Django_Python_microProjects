from django.conf.urls import url   # this gives us acess to the function url
from . import views           # This line is new! This explicitly imports views.py in the current folder
urlpatterns = [
    url(r'^$', views.index)   # This line has changed! Notice that urlpatterns is a list, the comma is in
]    # anticipation of all the routes that will be coming soon