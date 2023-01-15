from rest_framework.serializers import ModelSerializer
from .models import Client, Contract, Event, User, Staff


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'user_id']

class StaffDetailSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user_id']

class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'client_id']

class ContractDetailSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name']

class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
