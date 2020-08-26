from django.urls import path
from . import views

urlpatterns = [
    path('signupSubmit', views.signupSubmit, name="submit")
]
