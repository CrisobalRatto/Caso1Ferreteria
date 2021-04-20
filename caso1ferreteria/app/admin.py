from django.contrib import admin
from .models import Producto, Region, Comuna, TipoProducto, FamiliaProducto, Proveedor

#Superusuario: ferme
#Contraseña: ferme

admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoProducto)
admin.site.register(FamiliaProducto)
admin.site.register(Proveedor)