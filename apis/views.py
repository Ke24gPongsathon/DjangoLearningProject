from apis import utils
import os
from rest_framework import status
from rest_framework.response import Response
from django.db.models.functions import Concat
from safedelete.models import SOFT_DELETE_CASCADE
from django.utils.html import strip_tags
import json
from apis.serializers import UserSerializer, AddressSerializer
from apis.models import User, Address

from rest_framework import viewsets
# from rest_framework.views import APIView

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from apis.filters import UserFilter
from djangoLearningProject.task import send_email_task


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    
    file_name = 'detail.txt'
    
    def perform_create(self, serializer):
        serializer.save()
        self.send_email_to_user(serializer)
        
    def create_detail_txt(self, user):
        with open(self.file_name, "w+") as file:
            file.write(f"Email: {user.email}\n")
            file.write(f"Name: {user.name}\n")
            file.write(f"ID: {user.citizen_id}\n")
            file.write(f"Gender: {user.gender}\n")
            file.write(f"House Number: {user.address.house_number}\n")
            file.write(f"Village: {user.address.village}\n")
            file.write(f"Road: {user.address.road}\n")
            file.write(f"Sub District: {user.address.sub_district}\n")
            file.write(f"District: {user.address.district}\n")
            file.write(f"Province: {user.address.province}\n")
            file.write(f"Zip Code: {user.address.zip_code}\n")
                
            file.close()
    
    def send_email_to_user(self, serializer):
        user = serializer.instance
        
        self.create_detail_txt(user)
        
        html_content = render_to_string('email_create.html', serializer.data)
        text_content = strip_tags(html_content)
        
        email = EmailMultiAlternatives(
            subject='Your email subject',
            body=text_content,
            to=[self.request.user.email],
        )
        email.attach_file(self.file_name)
        email.attach_alternative(html_content, 'text/html')
        email.send()
        # send_email_task.delay("Test delay mail", email, "nore@example.com", [self.request.user.email])
        os.remove(self.file_name)
        
        return Response({'status': 'success'})
    
    
class UserDetailViewSet(UserViewSet):
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    

    
class AddressViewSet(viewsets.ModelViewSet):
    
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    