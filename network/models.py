from django.db import models
from django.conf import settings
from django.utils import timezone


LEVELS = ((0, 'Factory'), (1, 'Retail network'), (2, 'Sole proprietor'))

class Contact(models.Model):
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    country = models.CharField(max_length=255, verbose_name='Country')
    city = models.CharField(max_length=255, verbose_name='City')
    street = models.CharField(max_length=255, verbose_name='Street', 
                              blank=True, null=True)
    house_number = models.CharField(max_length=10, verbose_name='House number',
                              blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, 
                                verbose_name='Creator', null=True,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Supplier(models.Model):

    company_name = models.CharField(max_length=99, verbose_name='Company name')
    level = models.CharField(choices=LEVELS, verbose_name='level', default=0)
    contacts = models.OneToOneField(Contact, on_delete=models.CASCADE,
                                    verbose_name='Contacts',
                                    blank=True, null=True)
    supplier_name = models.ForeignKey('Supplier', on_delete=models.SET_NULL,
                                      verbose_name='Supplier name',
                                      blank=True, null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                               verbose_name='DEBT')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Owner',
                              on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.company_name}"


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    model = models.CharField(max_length=255, verbose_name='Model')
    launched_at = models.DateField(verbose_name='Launched at', 
                                   blank=True, null=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE,
                                 verbose_name='Supplier',
                                 blank=True, null=True)

    def __str__(self):
        return f"{self.model}"
