import urllib

from rest_framework import serializers

from apis import utils
from apis.models import User, Address


from django.db import IntegrityError

from djangoLearningProject import settings

class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = '__all__'