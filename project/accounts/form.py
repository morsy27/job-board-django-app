from dataclasses import fields
import email
from pyexpat import model
from tabnanny import check
from turtle import textinput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'placeholder':'Email....'})
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter First Name",
        widget=forms.TextInput(attrs={'placeholder':'Frist Name...'})
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter Last Name",
        widget=forms.TextInput(attrs={'placeholder':'Last Name...'})
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text="Enter Username",
        widget=forms.TextInput(attrs={'placeholder':'username...'})
    )
    password1 = forms.CharField(
        required=True,
        help_text="Enter Password",
        widget=forms.TextInput(attrs={'placeholder':'Password...','type' : 'password'})
    )
    password2 = forms.CharField(
        required=True,
        help_text="Enter Password again",
        widget=forms.TextInput(attrs={'placeholder':'Password again...','type' : 'password'})
    )
    
    check = forms.BooleanField(required=True)
    
    class Meta:
        model = User
        fields = [
            'username','email','first_name','last_name','password1','password2','check',
        ]