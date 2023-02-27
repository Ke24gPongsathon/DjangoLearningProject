from apis import utils
from rest_framework import status
from rest_framework.response import Response
from django.db.models.functions import Concat
from safedelete.models import SOFT_DELETE_CASCADE
from django.shortcuts import get_object_or_404

from apis.serializers import UserSerializer, AddressSerializer
from apis.models import User, Address

from rest_framework import generics, viewsets
# from rest_framework.views import APIView

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'
    # permission_classes = []
    
    def perform_create(self, serializer):
        serializer.save()
        self.send_email_to_user(serializer)
        
    
    def send_email_to_user(self, serializer):
        # context = {'user': user}
        from django.utils.html import strip_tags
        html_content = render_to_string('email_create.html', serializer.data)
        text_content = strip_tags(html_content)
        
        email = EmailMultiAlternatives(
            subject='Your email subject',
            body=text_content,
            to=[self.request.user.email],
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({'status': 'success'})

    
class AddressSerializer(viewsets.ModelViewSet):
    
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    