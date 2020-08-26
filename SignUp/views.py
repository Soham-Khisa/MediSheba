from django.shortcuts import render


# Create your views here.

def signupSubmit(request):
    usertype = request.POST['User']
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['pass']
    confirm = request.POST['cpass']
    print(usertype)
    print(firstname)
    print(lastname)
    print(email)
    print(phone)
    print(password)
    print(confirm)

    if usertype == 'user':
        return render(request, "UserHome.html")
    elif usertype == 'doctor':
        return render(request, "DoctorHome.html")
    elif usertype == 'hospitalAdmin':
        return render(request, "HospitalAdminHome.html")
    elif usertype == 'pharmacyManager':
        return render(request, "PharmacyManagerHome.html")
    elif usertype == 'bloodbankAdmin':
        return render(request,"BloodbankAdminHome.html")
