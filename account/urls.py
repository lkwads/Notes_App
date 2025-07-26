from . import views
from django.urls import re_path as url
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'account'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<slug>[-\w]+)/$', views.profiel, name='profiel'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<slug>[-\w]+)/change_password$', views.change_password, name='change_password'),

]

