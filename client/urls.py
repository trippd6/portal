from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/', views.user_login, name='login'),
    url(r'logout/', views.user_logout, name='logout'),
    url(r'site/(?P<id>[0-9]+)/$', views.site, name='site'),
]
