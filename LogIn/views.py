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
            return HttpResponse("Database Error or You don't exist")

    elif user == "User":
        statement = "SELECT USER_ID, PASSWORD from MEDI_SHEBA.USERS WHERE EMAIL=" + "\'" + email + "\'"
        c.execute(statement)
        if c:
            x = c.fetchone()
            return_id = x[0]
            return_password = x[1]
            # print(return_id)
            # print(return_password)

            decoded_password = decoder.EncryptPasswords(return_password).decryptPassword()

            if decoded_password == password:
                return render(request, "homepage/UserHome2.html")
            else:
                return HttpResponse("Wrong Pass")
        else:
            return HttpResponse("Database Error or You don't exist")

    elif user == "HospitalAdmin":
        statement = "SELECT HOSPITAL_ID,PASSWORD from MEDI_SHEBA.HOSPITAL WHERE EMAIL=" + "\'" + email + "\'"
        c.execute(statement)
        if c:
            x = c.fetchone()
            return_id = x[0]
            return_password = x[1]
            # print(return_id)
            # print(return_password)

            decoded_password = decoder.EncryptPasswords(return_password).decryptPassword()

            if decoded_password == password:
                return render(request, "homepage/HospitalAdminHome2.html")
            else:
                return HttpResponse("Wrong Pass")
        else:
            return HttpResponse("Database Error or You don't exist")

    elif user == "BloodBankAdmin":
        statement = "SELECT BLOOD_BANK_ID,PASSWORD from MEDI_SHEBA.BLOOD_BANK WHERE EMAIL=" + "\'" + email + "\'"
        c.execute(statement)
        if c:
            x = c.fetchone()
            return_id = x[0]
            return_password = x[1]
            # print(return_id)
            # print(return_password)

            decoded_password = decoder.EncryptPasswords(return_password).decryptPassword()

            if decoded_password == password:
                return render(request, "homepage/BloodbankHome2.html")
            else:
                return HttpResponse("Wrong Pass")
        else:
            return HttpResponse("Database Error or You don't exist")
    return render(request, "auth/LogInOrSignUp.html")


def signup(request):
    return render(request, "auth/SignUp.html")
