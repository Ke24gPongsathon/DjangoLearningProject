from django.urls import path, include
# from django.views.generic import TemplateView
from . import views



urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'list'}), name='user-list'),
]
