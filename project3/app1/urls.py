from django.urls import path
from . import views
urlpatterns = [
    path('',views.student),
    path('views/',views.student_view),
]