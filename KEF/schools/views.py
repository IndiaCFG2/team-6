from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, "main_page/main.html")

def profile(request):
    return render(request,"main_page/profile.html")

def allcourses(request):
    return render(request,"schools/teacher/allcourses.html")


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
    return render(request, 'schools/register.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        email_id = request.POST['email']
        password_id = request.POST['password']
        user = Teacher.objects.filter(email = email_id).first()

        if user is not None:
            return redirect('index')

        else:
            messages.info(request,'Invalid username or password!')
            return redirect('login')

    else:
        return render(request,"schools/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
