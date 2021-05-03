"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def registro(request):
    """Renders the register page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registro.html',
        {
            'title':'Registro',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def catalogo(request):
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/catalogo.html',
        {
            'title':'Catalogo',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def carro(request):
    """Renders the cart page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/carro.html',
        {
            'title':'Carro',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def user(request):
    """Renders the user page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user.html',
        {
            'title':'User',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )