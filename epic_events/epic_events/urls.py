"""softdesk URL Configuration

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
from rest_framework import routers
from events.views import (
    ClientViewset,
    ContractViewset,
    EventViewset,
    StaffViewset,
    UserViewset)

router = routers.SimpleRouter()
router.register('users', UserViewset, basename='users')
router.register('staffs', StaffViewset, basename='staffs')
router.register('clients', ClientViewset, basename='clients')
router.register('contracts', ContractViewset, basename='contracts')
router.register('events', EventViewset, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
