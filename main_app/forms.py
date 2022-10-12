from django.contrib.auth.forms import UserCreationForm
from .models import Chef, Client
from django import forms

class RegisterChefForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Chef
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class RegisterClientForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Client
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
