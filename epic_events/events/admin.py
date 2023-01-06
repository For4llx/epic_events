from django.contrib import admin
from .models import Client, Staff, Contract, Event

admin.site.register([Client, Staff, Contract, Event])
