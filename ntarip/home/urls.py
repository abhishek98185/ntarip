from django.contrib import admin
from django.urls import path
from .views import index,jeeadvance


urlpatterns = [
    path('', index , name='home'),
    path('jeeadvance',jeeadvance,name="jeeadvance")
]

