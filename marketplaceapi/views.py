from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products, Users, Categorys
from .serializers import CategorysSerializer, ProductsSerializer, UsersSerializer, CPSerializer

from django.core.serializers.json import DjangoJSONEncoder



# Create your views here.

def index(request):
    return HttpResponse('<h1>martketplace api</h1>')



class UsersList(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    # return HttpResponse('Working')



class CategoriesList(APIView):
    def get(self,request):
        categories = Categorys.objects.all()
        serializer = CategorysSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self,request):
        name_c = CategorysSerializer(data=request.data)        
        if name_c.is_valid():
            name_c.save()
        return Response(name_c,status=status.HTTP_201_CREATED)


class ProductsList(APIView):
    def get(self,request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products,many=True)
        return Response(serializer.data)
    def post(self,request):
            return Response(request.data)



class CPList(APIView):
    def get(self, request):
        return HttpResponse('<h1>working</h1>')
        # serializer_class = CPList
        # return Response(serializer_class)


