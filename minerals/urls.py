from django.urls import path
from django.contrib import admin

from . import views

app_name= "minerals"

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('<int:pk>/', views.mineral_detail, name='detail'),
]