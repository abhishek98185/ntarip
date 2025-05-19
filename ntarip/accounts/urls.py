from django.contrib import admin
from django.urls import path
from .views import loginUser,logoutUser,registration

urlpatterns = [
    path('/login', loginUser, name='login'),
    path('/logout', logoutUser, name='logout'),
    path('/register', registration, name='register')
]
