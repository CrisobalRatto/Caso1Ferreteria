"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, get_object_or_404
from app.models import Usuario, Producto, FamiliaProducto #importar modelo para registrar en db
from django.http import HttpRequest
from app import views
from django.core.mail import send_mail
from cart.forms import CartAddProductForm


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
    if request.method == 'POST':
        mesagge_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        #send email
        send_mail(
            message_name,
            message,
            message_email,
            ['proyecto.ferme@gmail.com'],
            )
        return render(request, 'contact.html')

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




#def shopping(request):
#    """Renders the shopping cart page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'main/shopping-cart.html',
#        {
#            'title':'Carro de compras',
#            'message':'carro de compras.',
#            'year':datetime.now().year,
#            'shopping_page': 'active',
#        }
#    )

#def payment(request):
#    """Renders the payment  page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'main/payment-page.html',
#        {
#            'title':'Pago',
#            'message':'pague aqui.',
#            'year':datetime.now().year,
#            'register_page': 'active',
#        }
#    )

def product_list(request, category_slug=None):
    category = None
    categories = FamiliaProducto.objects.all()
    products = Producto.objects.filter()
    if category_slug:
        category = get_object_or_404(FamiliaProducto, slug=category_slug)
        products = Producto.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'product/list.html', context)



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'product/detail.html', context)



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
