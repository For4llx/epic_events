from rest_framework.serializers import ModelSerializer
from .models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_user']

class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
