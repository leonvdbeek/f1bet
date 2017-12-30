from django.urls import path, re_path
from . import views

urlpatterns = [

    # /home/
    path('', views.index, name='index'),

    # /f1better/index.html
    path('index.html', views.index, name='index'),

    path('register', views.register, name='register'),
    path('register.html', views.register, name='register'),

    path('login', views.login, name='login'),
    path('login.html', views.login, name='login'),

    path('logout', views.logout, name='logout'),
]