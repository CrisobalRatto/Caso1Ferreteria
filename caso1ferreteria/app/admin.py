from django.contrib import admin
from .models import Producto, Region, Comuna, TipoProducto, FamiliaProducto, Proveedor, Usuario

#Superusuario: ferme
#Contrasena: ferme

admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoProducto)
admin.site.register(FamiliaProducto)
admin.site.register(Proveedor)
admin.site.register(Usuario)