from django.shortcuts import render


# Create your views here.

def signupSubmit(request):
    return render(request, "UserHome.html")
