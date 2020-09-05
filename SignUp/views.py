import cx_Oracle
from django.shortcuts import render
import random
from django.contrib import messages


# Create your views here.

def signupSubmit(request):
    usertype = request.POST['User']
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['pass']
    confirm = request.POST['cpass']
    if password != confirm:
        return render(request, "SignUp.html", {'error_message': "Passwords Doesn't Match"})
    elif usertype == 'doctor':
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
        conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
        c = conn.cursor()
        c1 = conn.cursor()
        c2 = conn.cursor()

        statement = "INSERT INTO MEDI_SHEBA.DOCTORS(FIRST_NAME, LAST_NAME, EMAIL, PHONE) VALUES (" + "\'" + firstname + \
                    "\', " + "\'" + lastname + "\'," + "\'" + email + "\', " + "\'" + phone + "\'" + ")"
        c.execute(statement)
        conn.commit()
        # print("SUCCESS INSERTING INTO DOCTORS")

        statement2 = "SELECT DOCTOR_ID FROM MEDI_SHEBA.DOCTORS WHERE EMAIL =" + "\'" + email + "\'"

        c1.execute(statement2)

        temp = 0
        for x in c1:
            temp = x
        print(temp[0])

        statement3 = "INSERT INTO MEDI_SHEBA.DOCTOR_AUTHENTICATION(DOCTOR_ID, EMAIL, PASSWORD) VALUES (" + str(
            temp[0]) + "," \
                     + "\'" + email + "\'," + "\'" + password + "\'" + ")"
        c2.execute(statement3)
        conn.commit()

        return render(request, "DoctorHome.html")

    elif usertype == 'user':
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
        conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
        c = conn.cursor()
        statement = "INSERT INTO MEDI_SHEBA.USERS(FIRST_NAME, LAST_NAME, EMAIL, PHONE) VALUES (" + "\'" + firstname + \
                    "\', " + "\'" + lastname + "\'," + "\'" + email + "\', " + "\'" + phone + "\'" + ")"
        c.execute(statement)
        conn.commit()
        print(statement)
        print("SUCCESS INSERTING INTO USERS")
        return render(request, "UserHome.html")

    elif usertype == 'hospitalAdmin':
        return render(request, "HospitalAdminHome.html")

    elif usertype == 'pharmacyManager':
        return render(request, "PharmacyManagerHome.html")

    elif usertype == 'bloodbankAdmin':
        return render(request, "BloodbankAdminHome.html")
