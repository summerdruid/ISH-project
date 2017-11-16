from django.conf.urls import url
from viewer import views

urlpatterns = [url(r'^$', views.index, name='index'),
              url(r'^register/$',views.register, name='register'),
              url(r'^newindex/$', views.newindex, name='newindex'),
			  url(r'^login/$', views.user_login, name='login'),
              url(r'^logout/$', views.user_logout, name='logout'),
			  url(r'^account/(?P<username>\w+)/$', views.account, name='account'),
			  url(r'^editAccount/$', views.editAccount, name='editAccount'),
			  url(r'^createRoute/$', views.createRoute, name='createRoute'),
			  url(r'^loadRoute/$', views.loadRoute, name='loadRoute'),
			  url(r'^routeHistory/$', views.routeHistory, name='routeHistory'),
			  url(r'^viewGraphs/$', views.viewGraphs, name='viewGraphs'),		# url needs changing for graphs of different routes, was unsure what it should be
			  url(r'^viewRoute/$', views.viewRoute, name='viewRoute'),		# url needs changing for viewing different routes, was unsure what it should be
			  ]
