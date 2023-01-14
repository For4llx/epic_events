from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer, ClientDetailSerializer
from authentification.models import User
from .models import Client
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ClientViewset(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
