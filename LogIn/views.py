from django.http import HttpResponse
from django.shortcuts import render
import cx_Oracle

import HelperClasses.encryptPass as decoder


# Create your views here.

def login(request):
    return render(request, "auth/LogInOrSignUp.html")


def submit(request):
    email = request.POST['email']
    password = request.POST['pass']
    user = request.POST['User']

    print("EMAIL: " + email)
    print("PASS: " + password)
    print("User Type: " + user)

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
    conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)

    # shamim change here

    # dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
    # conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)

    # ------#

    c = conn.cursor()

    # TODO: connect database and verify
    if user == "Doctor":
        statement = "SELECT DOCTOR_ID, PASSWORD from MEDI_SHEBA.DOCTOR WHERE EMAIL=" + "\'" + email + "\'"
        c.execute(statement)
        if c:
            x = c.fetchone()
            return_id = x[0]
            return_password = x[1]
            # print(return_id)
            # print(return_password)

            decoded_password = decoder.EncryptPasswords(return_password).decryptPassword()

            if decoded_password == password:
                return render(request, "homepage/DoctorHome2.html")
            else:
                return HttpResponse("Wrong Pass")
        else:
            print("NOT FOUND")  # TODO: DEBUG NOT PRINTING

    elif user == "User":
        return render(request, "homepage/UserHome.html")
    elif user == "HospitalAdmin":
        return render(request, "homepage/HospitalAdminHome.html")
    return render(request, "auth/LogInOrSignUp.html")


def signup(request):
    return render(request, "auth/SignUp.html")
