# sistema_biblioteca_app/forms.py
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ConfirmacionPrestamoForm(forms.Form):
    confirmacion = forms.BooleanField(label='Confirmo que deseo solicitar el préstamo de este libro', required=True)