# to see data from db in api we create serializer

from rest_framework.serializers import ModelSerializer
from frontend.models import portfolio


class PortfoliosSe(ModelSerializer):
    class Meta:
        model = portfolio
        fields = '__all__'
class PublicPortfoliosSe(ModelSerializer):
    
    class Meta:
        model = portfolio
        fields = ['time','title','desc','imgs']

        
      
        
        