from django.conf.urls import url
from viewer import views

urlpatterns = [url(r'^$', views.index, name='index')]
