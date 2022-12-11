
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.adminPage.as_view(),name='admin'),
    path('delete/<slug:data>/', views.deleteQuestion.as_view(),name='deleteMisc'),
    path('edit/<slug:data>/', views.EditQuestion.as_view(),name='editMisc'),
]
