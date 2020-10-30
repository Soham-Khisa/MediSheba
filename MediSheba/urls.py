from django.contrib import admin
from django.urls import path, include
from Doctors import views as doctor_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("LogIn.urls")),
    path('', include("Users.urls")),
    path('', include("SignUp.urls")),
    path('change_profile', doctor_view.doctor_edit_profile, name='doctor_edit_profile'),
    path('settings', doctor_view.doctor_settings, name='doctor_settings'),
    path('logout', doctor_view.logout, name='logout')

]
