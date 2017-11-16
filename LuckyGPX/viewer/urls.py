from django.conf.urls import url
from viewer import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newindex/$', views.newindex, name='newindex'),
    url(r'^test/$', views.test, name='test'),
]
