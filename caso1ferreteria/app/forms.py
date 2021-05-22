"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
##from .models Usuario
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


##class formlog(forms.ModelForm):
    ##class Meta:
        ##model = Usuario
        ##fields = ['nombre_usuario', 'contrasena', 'id_tipousu']
