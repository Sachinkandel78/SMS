from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students':students
    }

    response = render(request,'index.html',context)
    response.set_cookie('visited','True')
    return response

def delete(request,id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
    return redirect("/")



from django.http import HttpResponse  
def create(request):
    if request.COOKIES.get('visited') == "True":
        return HttpResponse("Please go through the home page first before creating a student.")

    if request.method =="GET":
        return render(request,'create.html')
    
    name = request.POST.get('name')
    roll = request.POST.get('roll')
    age = request.POST.get('age')
    Class = request.POST.get('Class')
    Student.objects.create(
        name = name,
        roll = roll,
        age = age,
        Class = Class
    )
    return redirect('/')

#https://github.com/hehenischal/sms


def update(request,id):
    
    if request.method =="GET":
        student = Student.objects.get(id=id)
        context = {
            'student':student
        }
        return render(request,'update.html',context)
    
    student = Student.objects.get(id=id)
    student.name = request.POST.get('name')
    student.roll = request.POST.get('roll')
    student.age = request.POST.get('age')
    student.Class = request.POST.get('Class')
    student.save()
    
    return redirect('/')