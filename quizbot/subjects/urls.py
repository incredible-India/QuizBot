
from django.urls import path
from . import views

urlpatterns = [
    
    path('misc/', views.adminPage.as_view(),name='miscadmin'),
    path('misc/delete/<slug:data>/', views.deleteQuestion.as_view(),name='deleteMisc'),
    path('misc/edit/<slug:data>/', views.EditQuestion.as_view(),name='editMisc'),
]
