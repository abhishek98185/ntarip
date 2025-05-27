from django.contrib import admin
from django.urls import path
from .views import exam

urlpatterns = [
    path('/paper/', exam, name='Paper')
]

