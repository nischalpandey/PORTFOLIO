from django.shortcuts import render ,redirect
from .models import portfolio as pf
from django.conf import settings

# Create your views here.
def home(request):

    return render(request, 'index.html')



def contact(request):
    if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
         port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = request.POST.get("subject")  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [request.POST.get("email"), ]  
           message = request.POST.get("name") +request.POST.get("body")  
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
           messages.success(request, request.POST.get("name")+ "Your Message sent." )
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