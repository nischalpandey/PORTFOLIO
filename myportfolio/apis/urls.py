from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('portfolio/public', publicapi.as_view(),name='public'),
    path('portfolio', ProjectView.as_view()),
   
    path('portfolio/<str:pk>', projectDetail.as_view()),
    
   
    
    
  
]