# Generated by Django 4.2.4 on 2023-10-04 02:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('car', 'CAR'), ('motorcycle', 'MOTOCYCLE'), ('tractor', 'TRACTOR'), ('truck', 'TRUCK'), ('bus', 'BUS')], max_length=20)),
                ('automaker', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)])),
            ],
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('cnpj', django_cpf_cnpj.fields.CNPJField(max_length=18)),
                ('addres', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('addres', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('pix', 'PIX'), ('online', 'Online'), ('debit card', 'Debit Card'), ('credit card', 'Credit Card'), ('bank transfer', 'Bank Transfer'), ('cash', 'Cash')], max_length=20)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pendent', 'Pendent'), ('canceled', 'Canceled')], max_length=20)),
                ('desc', models.DecimalField(decimal_places=2, max_digits=3)),
                ('final_value', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('purchase_value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sell_value', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workstation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceMaintence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('service_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.service')),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.clientuser')),
                ('workstation_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.workstation')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaintence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.product')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('auto_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.automobile')),
                ('reserve_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.reserve')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.employeeuser')),
            ],
        ),
        migrations.AddField(
            model_name='employeeuser',
            name='workstation_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.workstation'),
        ),
    ]