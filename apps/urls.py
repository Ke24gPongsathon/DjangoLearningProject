"""djangoLearningProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('apis.urls')),

]

# id ngDHYrXoWawHTUfFlMKK4z7OAa3Ma1Xm1WT1Y2ht
# secret JeQAtHV1A0ko3OcetTln55lGPtWZXoWO1usfX2NMIk63oVE0cN9tpQu0jEydzb1Ua4rhyaUANaFNCiKcmgnrAaEp5rgTz4YIIzYSU4HUo3ZTV31uds8YxR9YgNQrGsCS