from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from schools.forms import UserRegisterForm
from schools.models import School

def index(request):
    schools = School.objects.all()
    return render(request, 'employees/index.html', {'schools': schools})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')

    else:
        form = UserRegisterForm()
    return render(request, 'employees/register.html', {'form' : form})

def course(request):
    return render(request, 'employees/course.html')

def tcher(request):
    return render(request, 'employees/Tcher.html')
