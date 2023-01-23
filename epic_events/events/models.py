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
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMISSIONS, default='', max_length=50)

    def __str__(self):
        return self.user.email


class Client(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    sales_contact = models.ForeignKey(
        to=Staff,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    type = models.CharField(choices=TYPES, default='', max_length=50)

    def __str__(self):
        return self.user.email

class Contract(models.Model):
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        blank=True) 
    date_created = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS, default='', max_length=50)
    support = models.ForeignKey(
        to=Staff,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    contract = models.ForeignKey(
        to=Contract,
        on_delete=models.CASCADE,
        blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
