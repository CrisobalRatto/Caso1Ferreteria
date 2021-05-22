"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from app.models import Usuario #importar modelo para registrar en db
from django.http import HttpRequest

from django.contrib import messages 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'home_page': 'active',
        }
    )
##def home(reqiest):
##   return render_to_response('app/index.html')

def about(request):
    """Renders the about  page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,


        'app/about-us.html',
        {
            'title':'Acerca de nosotros',
            'message':'pague aqui.',
            'year':datetime.now().year,
            'about_page': 'active',
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact-us.html',
        {
            'title':'Contactenos',
            'message':'Pagina de contacto.',
            'year':datetime.now().year,
            'contact_page': 'active',
        }
    )

def register(request):
    """Renders the about Register page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'title':'Registración',
            'message':'Regístrese Aquí.',
            'year':datetime.now().year,
            'register_page': 'active',
        }
    )

def product(request):
    """Renders the about product page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/product-page.html',
        {
            'title':'Pagina producto',
            'message':'vea su producto.',
            'year':datetime.now().year,
            'product_page': 'active',
        }
    )

def catalog(request):
    """Renders the about catalog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/catalog-page.html',
        {
            'title':'Catalogo',
            'message':'Nuestros productos.',
            'year':datetime.now().year,
            'catalog_page': 'active',
        }
    )

def shopping(request):
    """Renders the shopping cart page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/shopping-cart.html',
        {
            'title':'Carro de compras',
            'message':'carro de compras.',
            'year':datetime.now().year,
            'shopping_page': 'active',
        }
    )

def payment(request):
    """Renders the payment  page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payment-page.html',
        {
            'title':'Pago',
            'message':'pague aqui.',
            'year':datetime.now().year,
            'register_page': 'active',
        }
    )






#registro usuario

def Userregistration(request):
    if request.method=='POST':
        if request.POST.get('id_usuario') and request.POST.get('nombre_usuario') and request.POST.get('contrasena') and request.POST.get('id_tipousu'): 
            saverecord=Usuario() 
            saverecord.id_usuario=request.POST.get('id_usuario')
            saverecord.nombre_usuario=request.POST.get('nombre_usuario')
            saverecord.contrasena=request.POST.get('contrasena')
            saverecord.id_tipousu=request.POST.get('id_tipousu')
            saverecord.save()
            messages.success(request,'Usuario registrado satisfactoriamente.')
            return render(request,'index.html')
        else:
            return render(request,'index.html')

