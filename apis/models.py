from django.db import models
from apis import utils

class Address(utils.BaseModel):
    house_number = models.CharField(max_length=100, default='', blank=True)
    village = models.CharField(max_length=100, default='', blank=True)
    road = models.CharField(max_length=100, default='', blank=True)
    sub_district = models.CharField(max_length=100, default='', blank=True)
    district = models.CharField(max_length=100, default='', blank=True)
    province = models.CharField(max_length=100, default='', blank=True)
    zip_code = models.CharField(max_length=5, default='', blank=True)
    
    def __str__(self):
        return f'{self.house_number} {self.village}' 
    

class User(utils.BaseModel):
    email = models.EmailField(max_length=255, default='', unique=True)
    name = models.CharField(max_length=100)
    citizen_id = models.CharField(max_length=13, unique=True)
    gender = models.IntegerField(choices=utils.GENDER_CHOICE, default=utils.MALE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="address_%(class)s")
    