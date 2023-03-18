from django.contrib import admin

# Register your models here.
from .models import portfolio
from .models import profile

class PortfolioAdmin(admin.ModelAdmin):
    list_display =("title","catg")
    prepopulated_fields = {"slug": ("catg","title")}
    search_fields =["title"]
    list_filter =['catg']
    
admin.site.register(portfolio,PortfolioAdmin)
admin.site.register(profile)