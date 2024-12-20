# Generated by Django 5.1.4 on 2024-12-16 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='House number')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=99, verbose_name='Company name')),
                ('level', models.CharField(choices=[(0, 'Factory'), (1, 'Retail network'), (2, 'Sole proprietor')], default=0, verbose_name='level')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='DEBT')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('contacts', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.contact', verbose_name='Contacts')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('supplier_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network.supplier', verbose_name='Supplier name')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('model', models.CharField(max_length=255, verbose_name='Model')),
                ('launched_at', models.DateField(blank=True, null=True, verbose_name='Launched at')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.supplier', verbose_name='Supplier')),
            ],
        ),
    ]
