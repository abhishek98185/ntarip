from django.contrib import admin
from django.urls import path
from .views import exam

urlpatterns = [
    path('/paper/<int:year>/<slug:paper>', exam, name='Paper')
]

