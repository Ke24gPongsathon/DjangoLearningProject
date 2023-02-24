import os
from django.db import models
from django.conf import settings
from django.core.paginator import Paginator
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    original_objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
MALE = 1
FEMALE = 2
GENDER_CHOICE = (
    (MALE, 'male'),
    (FEMALE, 'female')
)