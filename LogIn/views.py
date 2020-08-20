from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, "LogInOrSignUp.html")


def submit(request):
    email = request.GET['email']
    password = request.GET['pass']
    user = request.GET['User']

    print("EMAIL: " + email)
    print("PASS: " + password)
    print("User Type: " + user)

    # TODO: connect database and verify

    return render(request, "Home.html")


def signup(request):
    return render(request, "SignUp.html")
