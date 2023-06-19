from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        return HttpResponse(f"Name:{name}, Password:{pwd}")
    return render(request, "login.html")

def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        mail = request.POST['email id']
        pwd = request.POST['password']
        return HttpResponse(f"Name: {name}, Email: {mail},password:{pwd}")
    return render(request, "signup.html")

