
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.adminPage.as_view(),name='admin'),
]
