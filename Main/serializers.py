from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = ClientUser
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = EmployeeUser
        fields = '__all__'

class WorkstationSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Workstation
        fields = '__all__'

class AutomobileSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Automobile
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Service
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Product
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Payment
        fields = '__all__'

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Reserve
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Maintenance
        fields = '__all__'
        
class ProdMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = ProductMaintenance
        fields = '__all__'

class ServMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = ServiceMaintenance
        fields = '__all__'


    