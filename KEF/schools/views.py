from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "schools/teacher/landing_page.html")
