from apis import utils
from rest_framework import status
from rest_framework.response import Response
from django.db.models.functions import Concat
from safedelete.models import SOFT_DELETE_CASCADE
from django.shortcuts import get_object_or_404

from apis.serializers import UserSerializer, AddressSerializer
from apis.models import User, Address

from rest_framework import generics, viewsets
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'
    
    

    
class AddressSerializer(viewsets.ModelViewSet):
    
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    