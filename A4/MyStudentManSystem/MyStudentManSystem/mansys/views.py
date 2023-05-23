
from django.shortcuts import render
from .models import Faculty,Student
from django.shortcuts import redirect
from math import ceil
# import the logging library
import logging

#from django.http import HttpResponse
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
 #from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'mansys/index.html')

def registerfaculty(request):
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password= request.POST.get('password', '')

        username=request.POST.get('username', '')

        faculty = Faculty(name=name, email=email, password=password, username=username)
        faculty.save()
    return render(request, 'mansys/register.html')

def registerstudent(request):
    if request.method == "POST":
        name =request.POST.get('name','')
        email=request.POST.get('email','')
        password = request.POST.get('password', '')
        username = request.POST.get('username', '')

        rollNo=request.POST.get('rollNo','')

        student = Student(name=name, email=email, password=password, username=username,rollNo=rollNo)
        student.save()
    return render(request,'mansys/regstu.html')




def login(request):
    if request.method=='POST':
        student = request.POST.get('student', 'off')
        faculty = request.POST.get('faculty', 'off')
        if student == "on":
            un=request.POST.get('username','')
            ps=request.POST.get('password','')
            stu=Student.objects.get(username=un)
            if stu.password==ps:
                return render(request, 'mansys/main.html')
            else:
                return HttpResponse("hhh")
        if faculty == "on":
            un = request.POST.get('username', '')
            ps = request.POST.get('password', '')
            stu = Faculty.objects.get(username=un)
            if stu.password == ps:
                return render(request, 'mansys/main1.html')
            else:
                return HttpResponse("hhh")
    return render(request,'mansys/login.html')



















#def contact(request):
    #return HttpResponse("We are at contact")

