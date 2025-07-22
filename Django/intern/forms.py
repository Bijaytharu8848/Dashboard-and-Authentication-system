from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import intern


class Signupform(UserCreationForm):
    password1 =forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 =forms.CharField(label='Confirmpassword',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name' , 'email',]
        labels ={'first_name':'First Name','last_name':'Last Name',
                'email':'Email'}
        widgets ={'username':forms.TextInput(attrs={'class': 'form-control'}),
                  'first_name':forms.TextInput(attrs={'class': 'form-control'}),
                  'last_name':forms.TextInput(attrs={'class': 'form-control'}),
                  'email':forms.EmailInput(attrs={'class': 'form-control'}),
                  }
        
class Loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'placeholder': 'Enter your name','class':'form-group'}))
    password=forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autofocus':True,'placeholder': 'Enter your password','class':'form-group'}))
    
class PostEmployee(forms.ModelForm):
    class Meta:
        model=intern
        fields=['firstname', 'lastname','email','phone','location','college','job','myfile']   
        labels={'firstname':'First_Name','lastname':'last_Name','email':'Email', 'phone':'Phone','location':'Location',
                'college':'College','job':'Job_type','myfile':'My_file'
                
                
                }
        widgets ={'firstname':forms.TextInput(attrs={'class': 'form-control'}),
                  'lastname':forms.TextInput(attrs={'class': 'form-control'}),
                  'email':forms.EmailInput(attrs={'class': 'form-control'}),
                  'phone':forms.NumberInput(attrs={'class': 'form-control'}),
                  'location':forms.TextInput(attrs={'class': 'form-control'}),
                  'college':forms.TextInput(attrs={'class': 'form-control'}),
                  'job':forms.Select(attrs={'class': 'form-control'}),
                  
                  }