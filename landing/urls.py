from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from landing import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]
