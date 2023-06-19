from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login),
    path('home',views.home),
]