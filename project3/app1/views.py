from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def student(request):
    if (request.method=="POST"):
        id=request.POST["studentid"]
        name=request.POST["studentname"]
        age=request.POST["studentage"]
        gender=request.POST["studentgender"]
        studentclass=request.POST["studentclass"]
        Student.objects.create(
            student_id=id,
            student_name=name,
            student_age=age,
            student_gender=gender,
            student_class=studentclass

        )
        

        print(id)
        print(name)
        print(age)
        print(gender)
        print(studentclass)

    return render(request,"student.html")

def student_view(request):
    data=list(Student.objects.all().values())
    #print(data)
    return render(request,"views.html",{"student" : data} )