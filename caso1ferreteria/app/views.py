"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from app.models import Usuario #importar modelo para registrar en db
from django.http import HttpRequest
from app import views


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


        'main/about-us.html',
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
        'main/contact-us.html',
        {
            'title':'Contactenos',
            'message':'Pagina de contacto.',
            'year':datetime.now().year,
            'contact_page': 'active',
        }
    )

##def register(request):
 #   """Renders the about Register page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/registration.html',
 #       {
  #          'title':'Registración',
   #         'message':'Regístrese Aquí.',
    #        'year':datetime.now().year,
     #       'register_page': 'active',
      #  }
    #)

def product(request):
    """Renders the about product page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/product-page.html',
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
        'main/catalog-page.html',
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
        'main/shopping-cart.html',
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
        'main/payment-page.html',
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
        id_usuario=request.GET
        id_tipousu=request.GET
        nombre_usuario=request.POST['nombre_usuario']
        contrasena=request.POST['contrasena']



        Usuario(nombre_usuario=nombre_usuario,contrasena=contrasena).save()
        messages.success(request,'el usuatio'+request.POST['nombre_usuario']+'se guardo')
        return render(request,'app/registration.html')
    else:
        return render(request,'app/registration.html')
