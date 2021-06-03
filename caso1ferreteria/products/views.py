from django.shortcuts import render
from django.contrib import messages
from .models import FamiliaProducto,TipoProducto,Producto,Proveedor



# Create your views here.

def product(request):
    """Renders the about product page."""
    productos = Producto.objects.all()
    return render(
        request,
        'main/product-page.html',
        {
            'title':'Pagina producto',
            'message':'vea su producto.',
            'product_page': 'active',
            'productos' : productos
        }
    )



def catalogo_productos(request):
    productos = Producto.objects.all()
    return render(
        request,
        'products/catalog-page.html',
        {
            'title':'Catálogo',
            'message':'vea su producto.',
            'product_page': 'active',
            'productos' : productos
        }
    )

def catalogo_filtro(request):
    qs = Producto.objects.all()
    familia = FamiliaProducto.objects.all()
    familiaProducto = request.GET.get('familiaProducto')
    if is_valid_queryparam(familiaProducto):
        qs = qs.filter(FamiliaProducto=familiaProducto)
