from django.shortcuts import render ,redirect
from .models import portfolio as pf
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request):

    return render(request, 'index.html')



def contact(request):
    if request.method == "POST": 
        subject = request.POST.get("subject")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get("email")]
        message = request.POST.get("name") + request.POST.get("body")
        send_mail(
         subject=subject,
         message=message,
         from_email=email_from,
         recipient_list=recipient_list,
         fail_silently=False,
        )  
        messages.success(request,  "Your Message sent." )
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