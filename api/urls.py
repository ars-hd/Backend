from django.urls import path
from api import views

urlpatterns = [
    path('', views.helo),
    path('employees/', views.employees)
]