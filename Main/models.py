from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.utils import timezone
# Create your models here.

class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = CPFField(masked=True)
    cnpj = CNPJField(masked=True)
    addres = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_custom(sender, instance, created, **kwargs):
    if created:
        ClientUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_custom(sender, instance, created, **kwargs):
    instance.customuser.save()

class EmployeeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = CPFField(masked=True)
    workstation_fk = models.ForeignKey("Workstation", on_delete=models.CASCADE,)
    addres = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_custom(sender, instance, created, **kwargs):
    if created:
        EmployeeUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_custom(sender, instance, created, **kwargs):
    instance.customuser.save()

class Workstation(models.Model):
    name = models.CharField(max_length=200)
    availability = models.DateField

    def __str__(self):
        return self.name
    
class Automobile(models.Model):
    auto_types = [
        ("car", "CAR"),
        ("motorcycle", "MOTOCYCLE"),
        ("tractor", "TRACTOR"),
        ("truck", "TRUCK"),
        ("bus", "BUS"),
    ]

    type = models.CharField(choices=auto_types)
    automaker = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.Year

    def __str__(self):
        return self.model
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    value = models.DecimalField

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    cod = models.PositiveIntegerField(max_digits=5)
    purchase_value = models.DecimalField(max_digits=6, decimal_places=2)
    sell_value = models.DecimalField(max_digits=6, decimal_places=2)
    stock_unit = models.PositiveIntegerField

    def __str__(self):
        return self.name

class Payment(models.Model):
    payment_types = [
        ("pix", "PIX"),
        ("online", "Online"),
        ("debit card", "Debit Card"),
        ("credit card", "Credit Card"),
        ("bank transfer", "Bank Transfer"),
        ("cash", "Cash"),
    ]

    payment_status = [
        ("approved", "Approved"),
        ("pendent", "Pendent"),
        ("canceled", "Canceled"),
    ]

    type = models.CharField(max_length=20, choices=payment_types)
    status = models.CharField(max_length=20, choices=payment_status)
    desc = models.DecimalField(max_digits=3, decimal_places=2)
    final_value = models.DecimalField(max_digits=3, decimal_places=2)

class Reserve(models.Model):
    datetime = models.DateTimeField
    client = models.ForeignKey("ClientUser", on_delete=models.CASCATE)
    workstation_fk = models.ForeignKey("Workstation", on_delete=models.CASCATE)

    def __str__(self):
        return self.datetime
    
class Maintenance(models.Model):
    reserve_fk = models.ForeignKey("Reserve", on_delete=models.CASCATE)
    auto_fk = models.ForeignKey("Automobile", on_delete=models.CASCADE) 
    responsible = models.ForeignKey("EmployeeUser", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.total

class ProductMaintence(models.Model):
    unit = models.PositiveIntegerField
    product_fk = models.ForeignKey("Product", on_delete=models.CASCATE)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.sub_total

class ServiceMaintence(models.Model):
    unit = models.PositiveIntegerField
    service_fk = models.ForeignKey("Service", on_delete=models.CASCATE)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.sub_total