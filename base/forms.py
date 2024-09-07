from django import forms
from .models import *

class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Checkout
        fields=['name','email','phone','address','city','zipcode','country','payment']
        exclude=['host']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['Name','Email','Phone','Message']
        exclude=['host']
