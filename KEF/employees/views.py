from django.shortcuts import render

# Create your views here.
def index(request):

    emps = Employee.objects.all()

    return render(request, "index.html", {'emps': emps})