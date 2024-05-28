from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('input',views.input,name='input'),
    path('output', views.DropDown, name='DropDown')
]