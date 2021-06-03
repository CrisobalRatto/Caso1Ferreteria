from django.db import models

# Create your models here.

class FamiliaProducto(models.Model):
    id_familia = models.AutoField(primary_key=True)
    nombre_familia = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'familia_producto'

class TipoProducto(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tipo_producto'

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_familia = models.ForeignKey(FamiliaProducto, models.DO_NOTHING, db_column='id_familia')
    fecha_vencimiento = models.DateField(blank=True, null=True)
    id_tipo = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo')
    descripcion = models.CharField(max_length=100) #base de datos error en la o acento o no se
    precio_clp = models.IntegerField()
    precio_usd = models.IntegerField()
    stock = models.IntegerField() #revisar tutorial subir foto
    foto = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=50)
    rut_proveedor = models.CharField(max_length=10)
    celular = models.BigIntegerField()
    correo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'
