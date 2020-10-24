from django.shortcuts import render
import cx_Oracle
from django.http import HttpResponse


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
