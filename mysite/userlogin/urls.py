from django.contrib import admin
from django.urls import path
from . import views

app_name = 'userlogin'

urlpatterns = [
    path('', views.index, name ='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_check, name='login'),
    path('logout/', views.logout, name='logout'),

]