from django.db import models
from authentification.models import User

STATUS = [
    ('pending', 'Pending'),
    ('in progress', 'In progress'),
    ('done', 'Done')
]
TYPES = [
    ('potential', 'Potential'),
    ('existing', 'Existing'),
]

ROLES = [
    ('management', 'Management'),
    ('sales', 'Sales'),
    ('support', 'Support'),
]


class Staff(User):
    role = models.CharField(choices=ROLES, default='', max_length=50)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staffs"

    def __str__(self):
        return self.email


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    sales_contact = models.ForeignKey(
        to=Staff,
        on_delete=models.CASCADE)
    type = models.CharField(
        choices=TYPES, default='',
        max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        to=Staff,
        on_delete=models.CASCADE)
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE)
    status = models.BooleanField()
    amount = models.FloatField()
    payement_due = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client.company_name


class Event(models.Model):
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE)
    support_contact = models.ForeignKey(
        to=Staff,
        on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_status = models.CharField(choices=STATUS, default='', max_length=50)
    event_date = models.DateField()
    notes = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client.company_name
