from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from myapp.models import *
from django.contrib.auth.forms import UserCreationForm

class train_registration(forms.ModelForm):
    class Meta:
        model=train_reg
        fields='__all__'
        widgets={
            
        }
class admin_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=admin
        fields=UserCreationForm.Meta.fields +('fname','lname','email')
        widgets={
            
        }

class customer_form(forms.ModelForm):
    class Meta:
        model=customer
        fields='__all__'
        Widget={
            'date':forms.NumberInput(attrs={'type':'date'}),
            
        }
class bill(forms.ModelForm):
    class Meta:
        model=billing
        fields='__all__'
        Widget={
            'date':forms.NumberInput(attrs={'type':'date'}),
        }
