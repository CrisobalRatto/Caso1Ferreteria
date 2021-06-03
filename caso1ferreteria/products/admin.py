from django.contrib import admin
from .models import FamiliaProducto, TipoProducto, Producto, Proveedor


# Register your models here.
admin.site.register([FamiliaProducto,TipoProducto,Producto,Proveedor])