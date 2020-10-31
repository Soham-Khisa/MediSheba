from django.shortcuts import render
import cx_Oracle
from django.http import HttpResponse

'''
def doctors(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
    conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
    c = conn.cursor()
    print(c)
    print('Success')
    c.execute("SELECT * from MEDI_SHEBA.DOCTOR")
    out = ''
    for row in c:
        out += str(row) + ' \n '
    conn.close()
    return HttpResponse(out, content_type="text/plain")

'''


def doctor_edit_profile(request):
    return render(request, 'homepage/DoctorProfile.html')


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


def logout(request):
    return HttpResponse("Log Out")
