import cx_Oracle
from django.http import HttpResponse
from django.shortcuts import render
from .models import DoctorName


# Create your views here.

def seeDoc(request):
    docList = []

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
    conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
    c = conn.cursor()
    # print(c)
    # print('Success')
    c.execute("SELECT * from MEDI_SHEBA.DOCTORS")

    for row in c:
        docList.append(DoctorName(row[0], row[1], row[2], row[3]))
    conn.close()

    for obj in docList:
        print(obj.id)
        print(obj.first_name)

    return render(request, "DoctorName.html", {'doc': docList})
