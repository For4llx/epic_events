from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Staff, Client, Contract, Event


class IsSalesTeam(BasePermission):
    """
    Allow Sales team to all request method action
    on clients, contracts and events they manage.
    """
    def has_object_permission(self, request, view, obj):
        try:
            staff = Staff.objects.get(user_id=request.user.id)
        except Staff.DoesNotExist:
            staff = None
        if staff and staff.permission == 'sales':
            if isinstance(obj, Client):
                return obj.sales_contact == staff
            elif isinstance(obj, Contract):
                return obj.client.sales_contact == staff
            elif isinstance(obj, Event):
                return obj.contract.client.sales_contact == staff
        else:
            return False

class IsSupportTeam(BasePermission):
    """
    Allow Support team to all request method action
    on events they manage.
    """
    def has_object_permission(self, request, view, obj):
        try:
            staff = Staff.objects.get(user_id=request.user.id)
        except Staff.DoesNotExist:
            staff = None
        if staff and staff.permission == 'support':
            if isinstance(obj, Event):
                return obj.support == staff
        else:
            return False

class IsManagementTeam(BasePermission):
    """
    Allow Management team to all request method
    """
    def has_object_permission(self, request, view, obj):
        try:
            staff = Staff.objects.get(user_id=request.user.id)
        except Staff.DoesNotExist:
            staff = None
        if staff:
            return staff.permission == 'management'
        else:
            return False