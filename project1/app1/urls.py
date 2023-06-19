from django.urls import path
from . import views

urlpatterns = [
     path('home',views.home),
    path('add/<int:num1>/<int:num2>/', views.addition, name='addition'),
    path('subtract/<int:num1>/<int:num2>/', views.subtraction, name='subtraction'),
    path('multiply/<int:num1>/<int:num2>/', views.multiplication, name='multiplication'),
    path('div/<int:num1>/<int:num2>/', views.division, name='division'),
     path('mod/<int:num1>/<int:num2>/', views.division, name='modulus'),
    
]