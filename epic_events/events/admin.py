from django.contrib import admin
from .models import Client, Staff, Contract, Event, User

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    ordering = ['id']

    def get_queryset(self, request):
        staff = Staff.objects.get(user_id=request.user.id)
        if staff.permission == "sales":
            return super().get_queryset(request).filter(sales_contact=staff.id)
        elif staff.permission == "management":
            return super().get_queryset(request)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'permission')
    ordering = ['id']
    

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id')
    ordering = ['id'] 

    def get_queryset(self, request):
        staff = Staff.objects.get(user_id=request.user.id)
        if staff.permission == "sales":
            client = Client.objects.get(sales_contact=staff.id)
            return super().get_queryset(request).filter(client_id=client.id)
        elif staff.permission == "management":
            return super().get_queryset(request)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        staff = Staff.objects.get(user_id=request.user.id)
        if db_field.name == "client":
            kwargs["queryset"] = Client.objects.filter(sales_contact=staff.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    ordering = ['id']

    def get_queryset(self, request):
        staff = Staff.objects.get(user_id=request.user.id)
        if staff.permission == "support":
            return super().get_queryset(request).filter(support=staff.id)
        else:
            return super().get_queryset(request)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        staff = Staff.objects.get(user_id=request.user.id)
        clients = Client.objects.filter(sales_contact=staff.id)
        if db_field.name == "support":
            kwargs["queryset"] = Staff.objects.filter(permission="support")
        if db_field.name == "contract":
            kwargs["queryset"] = Contract.objects.filter(client__in=clients)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Client, ClientAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
