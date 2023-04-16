from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from frontend.models import portfolio
from .serializer import *
from rest_framework.views import APIView
import os
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import JSONRenderer
class publicapi(APIView):
 renderer_classes = [JSONRenderer]
 def get(self,request):
     
     portfolios =portfolio.objects.all()
     ser = PublicPortfoliosSe(portfolios, many=True)
     
     return Response({"baseurl":'',"data":ser.data})



  

class ProjectView(APIView):
  # authentication_classes = [BasicAuthentication]
  
  permission_classes = [IsAuthenticated]
  
  def get(self,request):
    portfolios =portfolio.objects.all()
    ser = PortfoliosSe(portfolios, many=True)
    return Response({"data":ser.data,
    'User': str(request.user),
            
            # None
            # 'auth': str(request.auth),
    })

  def portfolio(self,request):
    serializer = PortfoliosSe(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data )
    return Response(serializer.errors)  

class projectDetail(APIView):
  permission_classes = [IsAuthenticated]
  def get_object(self, pk):
        
        try:
            return portfolio.objects.get(pk=pk)
        except portfolio.DoesNotExist:
            raise Http404

  def get(self,request,pk):
     testmodel_object = self.get_object(pk)
     ser = PortfoliosSe(testmodel_object, many=False)
     return Response(ser.data)

  def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = PortfoliosSe(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors)     
  def delete(self, request, pk):
    testmodel_object = self.get_object(pk)
    os.remove( testmodel_object.imgs.path)
    testmodel_object.delete()
   
    return Response("portfolio Deleted")       