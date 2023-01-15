from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    ClientSerializer,
    ClientDetailSerializer,
    ContractSerializer,
    ContractDetailSerializer,
    EventSerializer,
    EventDetailSerializer,
    UserSerializer,
    UserDetailSerializer,
    StaffSerializer,
    StaffDetailSerializer)
from authentification.models import User
from .models import Client, Contract, Event, Staff
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsSalesTeam, IsSupportTeam, IsManagementTeam


class UserViewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer
    permission_classes = [IsManagementTeam]

    def get_serializer_class(self):
        """
        Every action will use a detail serializer
        except the listing of all the projects.
        """
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()


class StaffViewset(ModelViewSet):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    detail_serializer_class = StaffDetailSerializer
    permission_classes = [IsManagementTeam]

    def get_serializer_class(self):
        """
        Every action will use a detail serializer
        except the listing of all the projects.
        """
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ClientViewset(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [IsSalesTeam|IsManagementTeam]

    def get_serializer_class(self):
        """
        Every action will use a detail serializer
        except the listing of all the projects.
        """
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContractViewset(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsSalesTeam]

    def get_serializer_class(self):
        """
        Every action will use a detail serializer
        except the listing of all the projects.
        """
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()


class EventViewset(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [IsSalesTeam|IsSupportTeam]

    def get_serializer_class(self):
        """
        Every action will use a detail serializer
        except the listing of all the projects.
        """
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()
