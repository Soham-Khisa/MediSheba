from django.urls import path
from . import views

urlpatterns = [
    path('see_doctors', views.see_doctors, name='see_doctors'),
]
