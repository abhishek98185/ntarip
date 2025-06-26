from django.contrib import admin
from django.urls import path
from .views import (
    index, jeeadvance, jee, neet,
    formulasheet, about, todolist,
    contact, dashboard, profile, leadership
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index , name='home'),
    path('jeeadvance', jeeadvance, name="jeeadvance"),
    path('jee', jee, name="jee"),
    path('neet', neet, name="neet"),
    path('formulasheet', formulasheet, name="formulasheet"),
    path('about', about, name="about"),
    path('todolist', todolist, name="todolist"),
    path('contact', contact, name='contact'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('leadership', leadership, name='leadership'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
