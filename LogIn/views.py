from django.http import HttpResponse
from django.shortcuts import render
import cx_Oracle


# Create your views here.

def login(request):
    return render(request, "LogInOrSignUp.html")


def submit(request):
    email = request.POST['email']
    password = request.POST['pass']
    user = request.POST['User']

    print("EMAIL: " + email)
    print("PASS: " + password)
    print("User Type: " + user)

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
    conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
    c = conn.cursor()

    # TODO: connect database and verify
    if user == "Doctor":
        statement = "SELECT DOCTOR_ID from MEDI_SHEBA.DOCTOR WHERE EMAIL=" + "\'" + email + "\'" + \
                    "AND PASSWORD =" + "\'" + password + "\' "
        c.execute(statement)
        if c:
            temp = 0
            for x in c:
                temp = x
                print("DOCTOR ID:" + str(temp[0]))
                return render(request, "DoctorHome.html", {'user': email})
        else:
            print("NOT FOUND")  # TODO: DEBUG NOT PRINTING

    elif user == "User":
        return render(request, "UserHome.html")
    elif user == "HospitalAdmin":
        return render(request, "HospitalAdminHome.html")
    return render(request, "LogInOrSignUp.html")


def signup(request):
    return render(request, "registration.html")
