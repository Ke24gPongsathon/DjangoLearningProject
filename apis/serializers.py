import urllib

from rest_framework import serializers

from apis import utils
from apis.models import User, Address


from django.db import IntegrityError

from apps import settings



class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = [
            'house_number', 'village', 'road', 'sub_district',
            'district', 'province', 'zip_code'
        ]

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    created_at = serializers.DateTimeField(format="%d/%m/%Y", read_only=True)

    
    def to_representation(self, instance):
        user = super().to_representation(instance)
        user['gender'] = instance.get_gender_display()
        
        return user
    
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()
        
        user = User.objects.create(address=address, **validated_data)
        # user = User(address=address, **validated_data)
        return user
    
    def update(self, user, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address_serializer = AddressSerializer(instance=user.address, data=address_data)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save()
        

        user.email = validated_data.get('email', user.email)
        user.name = validated_data.get('name', user.name)
        user.citizen_id = validated_data.get('citizen_id', user.citizen_id)
        user.gender = validated_data.get('gender', user.gender)
        user.save()
        
        return user

    class Meta:
        model = User
        fields = [
            'email', 'name', 'citizen_id', 'gender', 'address', 'created_at'
        ]