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
    gender_in = request.POST['Gender']
    hospital_Name=request.POST['company']

    gender = ""
    if gender_in == "male":
        gender = "M"
    else:
        gender = "F"

    '''
    print("USER TYPE: " + usertype)
    print("F NAME: " + firstname)
    print("L NAME: " + lastname)
    print("EMAIL: " + email)
    print("PASS: " + password)
    print("C PASS: " + confirm)
    print("PHONE: " + phone)
    print("GENDER: " + gender)
    '''
    if usertype == 'doctor':

        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
        conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
        c = conn.cursor()

        statement = "INSERT INTO MEDI_SHEBA.DOCTOR(FIRST_NAME, LAST_NAME, EMAIL, PHONE,PASSWORD, GENDER) VALUES (" + "\'" + firstname + \
                    "\', " + "\'" + lastname + "\'," + "\'" + email + "\', " + "\'" + phone + "\', " + "\'" + password + "\', " + "\'" + gender + "\'" + ")"
        c.execute(statement)
        conn.commit()
        print("SUCCESS INSERTING INTO DOCTORS")

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
        dsn_tns=cx_Oracle.makedsn('localhost','1521',service_name='ORCL')
        conn=cx_Oracle.connect(user='MEDI_SHEBA',password='1234',dsn=dsn_tns)
        c=conn.cursor()
        statement="INSERT INTO MEDI_SHEBA.HOSPITAL(HOSPITAL_NAME,FIRST_NAME, LAST_NAME, EMAIL,PASSWORD, PHONE) VALUES (" + "\'" + hospital_Name+"\'"+firstname + \
                    "\', " + "\'" + lastname + "\'," + "\'" + email + "\', " + "\'" +password+"\'"+ phone + "\'" + ")"
        c.execute(statement)
        conn.commit()
        return render(request, "HospitalAdminHome.html")

    elif usertype == 'bloodbankAdmin':
        return render(request, "BloodbankAdminHome.html")
