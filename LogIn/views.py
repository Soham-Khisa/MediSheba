from django.http import HttpResponse
from django.shortcuts import render


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

    # TODO: connect database and verify
    if user == "Doctor":
        return render(request, "DoctorHome.html", {'user': email})
    elif user == "User":
        return render(request, "UserHome.html")
    elif user == "MediShopAdmin":
        return render(request, "MediShopAdminHome.html")
    return render(request, "HospitalAdminHome.html")


def signup(request):
    return render(request, "SignUp.html")
