from django.contrib.auth.models import User,Group 

from rest_framework import routers,serializers,viewsets
from .models import Products

#types of serializers 1)Class based Serializer (serializers.Seializer)
#                    ,2)ModelSerializer (Class)
#                     3)HyperlinkedModelSerializer
#Serializer define API representation
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=Group 
#         fields=['urls','name']


# class UserVeiwSet(viewsets.ModelViewSet): #ViewSets--define views
#     queryset=User.object.all()
#     serializer_class=UserSerializer



#Routers -->auto detect URL config

# router = routers.DefaultRouter()
# router.register(r'Users',UserVeiwSet)
