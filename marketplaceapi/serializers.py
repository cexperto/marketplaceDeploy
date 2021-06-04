from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Users, Categorys, Products


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id_u','first_name','last_name','email')
        # fields = '__all__'

class CategorysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorys
        fields = ('id_c','name_c')


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id_p','name_p','description_p','price','sku','stock','able')

class CPSerializer(serializers.ModelSerializer):    


    class Meta:
        model = Products
        exclude = ('able')
    
    
    def to_representation(self, instance):
        return {
            'id':instance.id_p,
            'name':instance.name_p,
            'description':instance.description_p,
            'category': instance.category_fk.name_c
        }
