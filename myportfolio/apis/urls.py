from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('portfolio/public', views.publicapi,name='public'),
    path('portfolio', ProjectView.as_view()),
   
    path('portfolio/<str:pk>', projectDetail.as_view()),
    
   
    
    
  
]