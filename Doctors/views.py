from django.shortcuts import render
import cx_Oracle
from django.http import HttpResponse
from HelperClasses import json_extractor


def doctor_edit_profile(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
    conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
    c = conn.cursor()
    statement = "SELECT HOSPITAL_NAME FROM MEDI_SHEBA.HOSPITAL"
    c.execute(statement)

    hospital_names = []

    for i in c:
        hospital_names.append(i[0])

    location_names = json_extractor.JsonExtractor('name').extract("HelperClasses/zilla_names.json")
    location_names.sort()

    return render(request, 'homepage/DoctorProfileEditor.html', {'hospital_names': hospital_names, 'locations':location_names})


def search_options(request):
    return HttpResponse("SEARCH HERE")


def view_appointments(request):
    return HttpResponse("Appointments Here")


def blood_bank_appointment(request):
    return HttpResponse("Blood Bank Appointment Here")


def view_calender(request):
    return HttpResponse("View Calender Here")


def view_records(request):
    return HttpResponse("view records")


def change_schedule(request):
    return render(request, 'schedule_editor/AddSchedule.html')


def logout(request):
    return HttpResponse("Log Out")
