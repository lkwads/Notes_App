from . import views
from django.urls import re_path as url
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'home'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(), {'template_name':'login.html'}, name='login'),
    url(r'^sign/$', views.register, name='register'),
]