from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from django.views.generic import TemplateView
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
# urlpatterns = [
#     path('users/', views.UserViewSet.as_view({'get': 'list'}), name='user-list'),
# ]

urlpatterns = [
    path('', include(router.urls))
]