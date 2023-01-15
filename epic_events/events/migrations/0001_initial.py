# Generated by Django 4.1.5 on 2023-01-15 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('potential', 'Potential'), ('existing', 'Existing')], default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('client_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.client')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('management', 'Management'), ('sales', 'Sales'), ('support', 'Support')], default='', max_length=50)),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in progress', 'In progress'), ('done', 'Done')], default='', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('contract_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.contract')),
                ('support', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.staff')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.staff'),
        ),
        migrations.AddField(
            model_name='client',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
