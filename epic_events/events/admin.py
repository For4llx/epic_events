from django.contrib import admin
from .models import Client, Staff, Contract, Event, User
from authentification.forms import UserCreationForm, UserChangeForm


class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    ordering = ('last_name',)
    search_fields = ('last_name', 'email')

    def get_queryset(self, request):
        staff = Staff.objects.get(id=request.user.id)
        if staff.role == "sales":
            return super().get_queryset(request).filter(sales_contact=staff.id)
        elif staff.role == "management":
            return super().get_queryset(request)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    ordering = ('last_name',)
    form = UserCreationForm
    update_form = UserChangeForm
    search_fields = ('last_name', 'email')
    readonly_fields = ('password',)

    def get_form(self, request, obj=None, **kwargs):
        if not obj is None:
            kwargs['form'] = self.update_form
        else:
            kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id','__str__')
    ordering = ['id'] 

    def get_queryset(self, request):
        staff = Staff.objects.get(id=request.user.id)
        if staff.role == "sales":
            client = Client.objects.get(sales_contact=staff.id)
            return super().get_queryset(request).filter(client_id=client.id)
        elif staff.role == "management":
            return super().get_queryset(request)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        staff = Staff.objects.get(id=request.user.id)
        if db_field.name == "client":
            kwargs["queryset"] = Client.objects.filter(sales_contact=staff.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ['id']

    def get_queryset(self, request):
        staff = Staff.objects.get(id=request.user.id)
        if staff.role == "support":
            return super().get_queryset(request).filter(support=staff.id)
        else:
            return super().get_queryset(request)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        staff = Staff.objects.get(id=request.user.id)
        clients = Client.objects.filter(sales_contact=staff.id)
        if db_field.name == "support":
            kwargs["queryset"] = Staff.objects.filter(role="support")
        if db_field.name == "contract":
            kwargs["queryset"] = Contract.objects.filter(client__in=clients)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Client, ClientAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
