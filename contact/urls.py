from django.contrib import admin
from django.urls import path
from contact import views

app_name = 'Contact'

urlpatterns = [
    path('', views.index, name="index"),
]