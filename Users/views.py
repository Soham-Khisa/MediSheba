import cx_Oracle
from django.http import HttpResponse
from django.shortcuts import render
from .models import DoctorName


# Create your views here.

def see_doctors(request):
    docList = []

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
    conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
    c = conn.cursor()
    c.execute("SELECT FIRST_NAME || ' ' || LAST_NAME,PHONE, GENDER, SPECIALIZATION, HOSPITAL_ID "
              "from MEDI_SHEBA.DOCTOR")
    index = 1
    for row in c:
        docList.append(DoctorName(index, row[0], row[1], row[2], row[3], row[4]))  # DoctorName is defined in models.py
        index = index + 1
    conn.close()

    return render(request, "query_pages/doctor_query.html", {'doc': docList})
