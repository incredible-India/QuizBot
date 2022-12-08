
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.adminPage,name='admin'),
]
