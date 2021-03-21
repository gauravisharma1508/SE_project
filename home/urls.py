from django.contrib import admin
from django.urls import path,include
import features
from .views import index,Register,Login,home,logout
from features import views
app_name='home'
urlpatterns = [

    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    #path('home', Home.as_view(), name='home'),
    
    ]