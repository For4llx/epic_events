from django.contrib import admin
from .models import Client, Staff, Contract, Event

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id')
    ordering = ['id']

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id')
    ordering = ['id']

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id')
    ordering = ['id']

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['id']


admin.site.register(Client, ClientAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
