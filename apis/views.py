import threading
from apis import utils
from django.db.models import F
from rest_framework import status
# from apis.utils import get_paginator
# from apis.filter import KanbanFilter, KanbanBacklogFilter
from django.db import IntegrityError
from rest_framework.response import Response
from django.db.models.functions import Concat
from safedelete.models import SOFT_DELETE_CASCADE
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, CharField, Value as V
from rest_framework.exceptions import PermissionDenied

from apis.serializers import UserSerializer
from apis.models import User, Address

from rest_framework import generics, viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer