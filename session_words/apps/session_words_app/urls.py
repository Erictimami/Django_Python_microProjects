from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^session_words$', views.session_words),
    url(r'^clear_session$', views.clear_session)
    
]