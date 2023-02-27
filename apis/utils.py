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

PERMISSION_LEVEL_NONE = 0
PERMISSION_LEVEL_VIEW_ONLY = 1
PERMISSION_LEVEL_GENERAL = 2
PERMISSION_LEVEL_ADMIN = 3
CHOICE_PERMISSION_LEVEL = (
    (PERMISSION_LEVEL_NONE, 'none'),
    (PERMISSION_LEVEL_VIEW_ONLY, 'view only'),
    (PERMISSION_LEVEL_GENERAL, 'document'),
    (PERMISSION_LEVEL_ADMIN, 'admin'),
)
