from django import urls
from django.contrib.auth.views import LoginView
from django.urls import path
from users import views as v

app_name = 'users'
urlpatterns = [
    # login page:
    #path(r'login/', LoginView.as_view(), {'template_name':'users/login.html'}, name='login'),
    path(r'register/', v.register, name="register")
]