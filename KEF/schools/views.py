from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Teacher
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, "schools/teacher/landing_page.html")

def login(request):
    if request.method == 'POST':
        email_id = request.POST['email']
        password_id = request.POST['password']
        user = Teacher.objects.filter(email = email_id).first()

        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.info(request,'Invalid username or password!')
            return redirect('login')

    else:
        return render(request,"schools/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
