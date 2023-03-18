from django.urls import path
from .views import*

urlpatterns = [
    path('', home,name="home"),
 
    path('contact', contact,name="contact"),
    path('portfolio', portfolio,name="portfolio"),
    path('portfolio/detail/<slug:slug>', portfoliodetail),
    path('about', about,name="about")
    
]
