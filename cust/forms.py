from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CreateUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'
        # you can specific fields
        # like this...
        # fields = ['Name', 'phone']

class profileUpdate(ModelForm):

    class Meta:
        model = Customer
        fields = ['Name', 'phone', 'email']

