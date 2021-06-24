"""
Definition of urls for caso1ferreteria.
"""

from datetime import datetime
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from main.views import IndexPageView

#from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views



#urlpatterns = [
#    path('', views.home, name='home'),
#    path('contact/', views.contact, name='contact'),
#    path('about/', views.about, name='about'),
#    path('usuarios/', include('django.contrib.auth.urls')),
#    path('usuarios/', include('usuarios.urls')),
#
#    path('register/', views.Userregistration, name='register'),
#    path('login/',
#         LoginView.as_view
#         (
#             template_name='app/login.html',
#             authentication_form=forms.BootstrapAuthenticationForm,
#             extra_context=
#             {
#                 'title': 'Log in',
#                 'year' : datetime.now().year,
#             }
#         ),
#         name='login'),
#    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
#    path('admin/', admin.site.urls),
#    path('catalog/', views.catalog, name='catalog'),
#    path('payment/', views.payment, name='payment'),
#    path('product/', views.product, name='product'),
#    path('shopping/', views.shopping, name='shopping'),

#]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
    #path('payment/', views.payment, name='payment'),
    
    #path('shopping/', views.shopping, name='shopping'),
    path('', IndexPageView.as_view(), name='index'),

    #path('i18n/', include('django.conf.urls.i18n')),
    

    path('cuentas/', include('accounts.urls')),
    path('', include('app.urls', namespace='app')),
    
]
