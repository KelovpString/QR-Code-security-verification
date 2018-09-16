from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tools.models import product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=True,queryset=product.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'product')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# Product Serializer -->
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields = ('id','no','name','comment','creatTime','updateTime')
        
owner = serializers.ReadOnlyField(source='owner.username')