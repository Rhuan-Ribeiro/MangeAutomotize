from django.contrib import admin
from .models import *

# Register your models here.
class detClientUser(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf', 'cnpj')
    list_display_links = ('id',)
    search_fields = ('id', 'user', 'cpf', 'cnpj')
    list_per_page = 10

admin.site.register(ClientUser, detClientUser)

class detEmployeeUser(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf')
    list_display_links = ('id',)
    search_fields = ('id', 'user', 'cpf')
    list_per_page = 10

admin.site.register(EmployeeUser, detEmployeeUser)

class detWorkstation(admin.ModelAdmin):
    list_display = ('id', 'stations', 'availability')
    list_display_links = ('id',)
    search_fields = ('id', 'stations', 'availability')
    list_per_page = 10

admin.site.register(Workstation, detWorkstation)

class detAutomobile(admin.ModelAdmin):
    list_display = ('id', 'type', 'model', 'year')
    list_display_links = ('id',)
    search_fields = ('id', 'type', 'model', 'year')
    list_per_page = 10

admin.site.register(Automobile, detAutomobile)

class detService(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
    list_display_links = ('id',)
    search_fields = ('id', 'name', 'value')
    list_per_page = 10

admin.site.register(Service, detService)

class detProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'cod', 'purchase_value', 'sell_value', 'stock_unit')
    list_display_links = ('id',)
    search_fields = ('id', 'name', 'cod')
    list_per_page = 10

admin.site.register(Product, detProduct)

class detPayment(admin.ModelAdmin):
    list_display = ('id', 'reserve_fk', 'type', 'status', 'final_value')
    list_display_links = ('id',)
    search_fields = ('id', 'reserve_fk', 'status')
    list_per_page = 10

admin.site.register(Payment, detPayment)

class detReserve(admin.ModelAdmin):
    list_display = ('id', 'datetime', 'client', 'workstation_fk')
    list_display_links = ('id',)
    search_fields = ('id', 'datetime', 'client', 'workstation_fk')
    list_per_page = 10

admin.site.register(Reserve, detReserve)

class detMaintenance(admin.ModelAdmin):
    list_display = ('id', 'reserve_fk', 'auto_fk', 'responsible', 'total')
    list_display_links = ('id',)
    search_fields = ('id', 'reserve_fk', 'auto_fk', 'responsible', 'total')
    list_per_page = 10

admin.site.register(Maintenance, detMaintenance)

class detProductMaintenance(admin.ModelAdmin):
    list_display = ('id', 'unit', 'product_fk', 'sub_total')
    list_display_links = ('id',)
    search_fields = ('id', 'product_fk')
    list_per_page = 10

admin.site.register(ProductMaintenance, detProductMaintenance)

class detServiceMaintenance(admin.ModelAdmin):
    list_display = ('id', 'unit', 'service_fk', 'sub_total')
    list_display_links = ('id',)
    search_fields = ('id', 'service_fk')
    list_per_page = 10

admin.site.register(ServiceMaintenance, detServiceMaintenance)