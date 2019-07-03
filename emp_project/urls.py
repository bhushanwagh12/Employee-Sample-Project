
from django.contrib import admin
from django.urls import path
from emp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', views.demo),
    path('date/',views.date),
    path('morning/',views.good_morning),
    path('template/',views.template),
    path('register/',views.reg),
    path('show/',views.disp),


]
