from django.shortcuts import render ,redirect
from .models import portfolio as pf

# Create your views here.
def home(request):

    return render(request, 'index.html')



def contact(request):
    return render(request,'contact.html')
def portfolio(request):
    context = {"portfolio":pf.objects.all()}
    return render(request,'portfolio.html',context=context)
def portfoliodetail(request,slug):
    context = {"data":pf.objects.get(slug=slug)}
    return render(request,'portfoliodetail.html',context)
def about(request):
    return render(request,'about.html')

def notfound(request,exception):
    return render(request,'404.html')