from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile_create/', views.profile_create),
    path('connect/', views.connect),
]
