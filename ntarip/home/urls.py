from django.contrib import admin
from django.urls import path
from .views import index,jeeadvance,jee,neet,formulasheet,about,todolist


urlpatterns = [
    path('', index , name='home'),
    path('jeeadvance',jeeadvance,name="jeeadvance"),
    path('jee',jee,name="jee"),
    path('neet',neet,name="neet"),
    path('formulasheet',formulasheet,name="formulasheet"),
    path('about',about,name="about"),
    path('todolist',todolist,name="todolist")
]

