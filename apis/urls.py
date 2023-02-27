from django.urls import path, include
from rest_framework.routers import DefaultRouter
import oauth2_provider.views as oauth2_views
# from django.views.generic import TemplateView
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
]