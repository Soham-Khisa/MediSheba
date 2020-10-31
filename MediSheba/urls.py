from django.contrib import admin
from django.urls import path, include
from Doctors import views as doctor_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("LogIn.urls")),
    path('', include("Users.urls")),
    path('', include("SignUp.urls")),

    path('doctor/change_profile', doctor_view.doctor_edit_profile, name='doctor_edit_profile'),
    path('doctor/search_options', doctor_view.search_options, name='search_options'),
    path('doctor/view_appointments', doctor_view.view_appointments, name='view_appointments'),
    path('doctor/blood_bank_appointment', doctor_view.blood_bank_appointment, name='blood_bank_appointment'),
    path('doctor/view_calender', doctor_view.view_calender, name='view_calender'),
    path('doctor/view_records', doctor_view.view_records, name='view_records'),
    path('doctor/logout', doctor_view.logout, name='log_out')

]
