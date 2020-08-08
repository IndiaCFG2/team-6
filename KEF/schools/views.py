from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, "schools/main page/main.html")

def profile(request):
    return render(request,"schools/main page/profile.html")

def about(request):
    return render(request,"schools/main page/about.html")

def contact(request):
    return render(request,"schools/teacher/course.html")

def contact(request):
    return render(request,"schools/teacher/allcourses.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid username or password!')
            return redirect('login')

    else:
        return render(request,'schools/landing_page.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
