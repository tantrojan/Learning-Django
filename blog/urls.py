from django.conf.urls import url
from . import views

urlpatterns = [
    # /blog/
    url(r'^$', views.index , name='index'),
    # /blog/345/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^addnew/$', views.addnew , name='addnew'), 
]
