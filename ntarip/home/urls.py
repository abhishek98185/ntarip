from django.contrib import admin
from django.urls import path
from .views import index,jeeadvance,jee


urlpatterns = [
    path('', index , name='home'),
    path('jeeadvance',jeeadvance,name="jeeadvance"),
    path('jee',jee,name="jee")
]

