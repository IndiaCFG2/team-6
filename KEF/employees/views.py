from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth 

def index(request):

    emps = Employee.objects.all()

    return render(request, "index.html", {'emps': emps})


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'schools/login.html')    

def logout(request):
    auth.logout(request)
    return redirect('/')   