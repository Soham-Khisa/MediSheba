from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("LogIn.urls")),
    path('', include("Users.urls")),
    path('', include("SignUp.urls"))

]
