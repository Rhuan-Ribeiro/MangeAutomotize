from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = CPFField(masked=True)
    cnpj = CNPJField(masked=True)
    address = models.CharField(max_length=200)  # Correção: 'addres' -> 'address'
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_client_user(sender, instance, created, **kwargs):
    if created:
        ClientUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_client_user(sender, instance, **kwargs):
    instance.clientuser.save()

class EmployeeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = CPFField(masked=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_employee_user(sender, instance, created, **kwargs):
    if created:
        EmployeeUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_employee_user(sender, instance, **kwargs):
    instance.employeeuser.save()

class Workstation(models.Model):
    stations = [
        ("workstation1", "WORKSTATION 1"),
        ("workstation2", "WORKSTATION 2"),
    ]
    name = models.CharField(max_length=200, choices=stations)
    availability = models.DateField()  # Correção: Adicionado os parênteses para criar um campo de data

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

    type = models.CharField(max_length=20, choices=auto_types)
    automaker = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)  # Correção: Removido o int()
        ]
    )

    def __str__(self):
        return self.model

class Service(models.Model):
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=6, decimal_places=2)  # Correção: Adicionado os parênteses para criar um campo decimal

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    cod = models.PositiveIntegerField()
    purchase_value = models.DecimalField(max_digits=6, decimal_places=2)
    sell_value = models.DecimalField(max_digits=6, decimal_places=2)
    stock_unit = models.PositiveIntegerField()

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

    reserve_fk = models.ForeignKey("Reserve", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=payment_types)
    status = models.CharField(max_length=20, choices=payment_status)
    desc = models.DecimalField(max_digits=3, decimal_places=2)
    final_value = models.DecimalField(max_digits=3, decimal_places=2)

    def __float__(self):
        return float(self.final_value)  # Correção: Converte para float

class Reserve(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)  # Correção: 'ClientUser' em vez de "ClientUser"
    workstation_fk = models.ForeignKey(Workstation, on_delete=models.CASCADE)  # Correção: 'Workstation' em vez de "Workstation"

    def __str__(self):
        return str(self.datetime)  # Correção: Converte para string

class Maintenance(models.Model):
    reserve_fk = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    auto_fk = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    responsible = models.ForeignKey(EmployeeUser, on_delete=models.CASCADE)  # Correção: 'EmployeeUser' em vez de "EmployeeUser"
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __float__(self):
        return float(self.total)

class ProductMaintenance(models.Model):
    unit = models.PositiveIntegerField()
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __float__(self):
        return float(self.sub_total)

class ServiceMaintenance(models.Model):
    unit = models.PositiveIntegerField()
    service_fk = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __float__(self):
        return float(self.sub_total)
