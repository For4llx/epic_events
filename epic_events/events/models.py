from django.db import models


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
    ('pending', 'Pending')
    ('in progress', 'In progress'),
    ('done', 'Done'),
]

class Client(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    client_user = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    phone = models.CharField(_(""), max_length=50)
    mobile = models.CharField(_(""), max_length=50)
    company_name = models.CharField(_(""), max_length=50)
    sales_contact = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES, default='', max_length=50)


class Staff(models.Model):
    staff_id =  models.BigAutoField(primary_key=True)
    staff_user = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMISSIONS, default='', max_length=50)


class Contract(models.Model):
    contract_id = models.BigAutoField(primary_key=True)
    client_id = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    event_id = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    contract_id = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    name = models.CharField(_(""), max_length=50)
    status = models.CharField(choices=STATUS, default='', max_length=50)
    event_staff = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
