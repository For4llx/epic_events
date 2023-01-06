from django.db import models
from authentification.models import User


TYPES = [
    ('potential', 'Potential'),
    ('existing', 'Existing'),
]

PERMISSIONS = [
    ('management', 'Management'),
    ('sales', 'Sales'),
    ('support', 'Support'),
]

STATUS = [
    ('pending', 'Pending'),
    ('in progress', 'In progress'),
    ('done', 'Done'),
]


class Staff(models.Model):
    staff_id =  models.BigAutoField(primary_key=True)
    staff_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True)
    permission = models.CharField(choices=PERMISSIONS, default='', max_length=50)


class Client(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    client_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    sales_contact = models.ForeignKey(
        to=Staff,
        on_delete=models.CASCADE,
        blank=True)
    type = models.CharField(choices=TYPES, default='', max_length=50)


class Event(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS, default='', max_length=50)
    support = models.ForeignKey(
        to=Staff,
        on_delete=models.CASCADE,
        blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Contract(models.Model):
    contract_id = models.BigAutoField(primary_key=True)
    client_id = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        blank=True)
    event_id = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        blank=True)
    date_created = models.DateTimeField(auto_now_add=True)