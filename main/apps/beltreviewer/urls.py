from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^books/(?P<id>\d+)$', views.review),
    url(r'^users/(?P<id>\d+)$', views.userlist),
    url(r'^process$', views.process),
    url(r'^logout$', views.clear)    # This line has changed!
]