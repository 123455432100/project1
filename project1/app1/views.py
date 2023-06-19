from django.shortcuts import render
def addition(request, num1, num2):
    result = num1 + num2
    return render(request, 'result.html', {'result': result})

def subtraction(request, num1, num2):
    result = num1 - num2
    return render(request, 'result.html', {'result': result})

def multiplication(request, num1, num2):
    result = num1 * num2
    return render(request, 'result.html', {'result': result})
def division(request, num1, num2):
    result = num1 / num2
    return render(request, 'result.html', {'result': result})
def home(request):
    return render(request,"home.html")
def division(request, num1, num2):
    result = num1 % num2
    return render(request, 'result.html', {'result': result})

