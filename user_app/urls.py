from django.conf.urls import url
from . import views
from user_app.views import UserList

urlpatterns = [
    url(r'^all', UserList.as_view()),
    url(r'^myuser/(?P<pk>[A-Za-z0-9]*)$', views.myuser),
    url(r'^delete/(?P<pk>[A-Za-z0-9]*)$', views.delete),
]
