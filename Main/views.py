from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django_filters import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from restfw_composed_permissions.base import BaseCOmposedPermission 


# Create your views here.
class ClientUserAPIView(ModelViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'cpf', 'cnpj']
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAdminUser]

class EmployeeUserAPIView(ModelViewSet):
    queryset = EmployeeUser.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'cpf']
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAdminUser]

class WorkstationAPIView(ModelViewSet):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'stations', 'availability']
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)
    
class WorkstationAPIView(ModelViewSet):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'stations', 'availability']
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

class AutomobileAPIView(ModelViewSet):
    queryset = Automobile.objects.all()
    serializer_class = AutomobileSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

class ServiceAPIView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

class PaymentAPIView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = Payment.objects.all()
        else:
            #o usuario que solicitou a API tem que ser o mesmo usuario que fez a reserva deste pagamento
            queryset = Payment.objects.filter(bookingFK__customUserFK__user__username=user.username)
        return queryset  
    
class ReserveAPIView(ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

class MaintenanceAPIView(ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

class  ProductMaintenanceAPIView(ModelViewSet):
    queryset =  ProductMaintenance.objects.all()
    serializer_class =  ProdMaintenanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    pagination_class = PageNumberPagination
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticatedOrReadOnly]

    @receiver(post_save, sender=ProductMaintenance)
    def update_product_quantity(sender, instance, created, **kwargs):
        if created:
            # Subtrair a quantidade usada do estoque do produto
            product = instance.product
            product.quantity -= instance.quantity_used
            product.save()