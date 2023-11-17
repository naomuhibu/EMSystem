from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import SeismicIntensity

class SeismicIntensityForm(ModelForm):
    class Meta:
        model = SeismicIntensity
        fields =  '__all__'
'''
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password'] 

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
'''