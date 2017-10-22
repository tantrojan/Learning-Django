from django.conf.urls import url
from . import views

urlpatterns = [
    # /blog/
    url(r'^$', views.index , name='index'),
    # /blog/345/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]
