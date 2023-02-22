from django.db import models
from apis import utils

class Address(utils.BaseModel):
    house_number = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    sub_district = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)

class User(utils.BaseModel):
    name = models.CharField(max_length=100)
    citizen_id = models.CharField(max_length=13)
    gender = models.IntegerField(choices=utils.GENDER_CHOICE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address_%(class)s")
