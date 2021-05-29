"""
Definition of urls for caso1ferreteria.
"""


from django.urls import path
from .views import UserRegisterView



urlpatterns = [
    path('register/', UserRegisterView.as_view(),  name='registertwo'),



]
