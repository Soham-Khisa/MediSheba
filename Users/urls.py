from django.urls import path
from . import views

urlpatterns = [
    path('seeDoc', views.seeDoc, name='seeDoc'),
]
