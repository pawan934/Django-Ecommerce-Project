from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class customerRegisternationform(UserCreationForm):
    email = forms.CharField(required=True, label="Email", widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))

    password2 = forms.CharField(label='Confirm Password (Again)', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Confirm Password'}))
    

    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username'}))

    class Meta:
     model = User
     fields = ['username', 'email', 'password1', 'password2',]

class LoginForm(AuthenticationForm):
   username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control', 'placeholder':'Enter Username'}))
   
   password = forms.CharField(label=_('password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control','placeholder':'Enter Password'}))

class mypasswordchangform(PasswordChangeForm):
   old_password = forms.CharField(label=_('Old password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control','placeholder':'Enter Password'}))
   
   new_password1 = forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control','placeholder':'Enter Password'}),help_text=password_validation.password_validators_help_text_html())

   new_password2 = forms.CharField(label=_('Confirm new password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control','placeholder':'Enter confirm Password'}))


class MypasswordrestForm(PasswordResetForm):
   email = forms.EmailField(label=_('Email'),required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Register Email'}))

class MysetForm(SetPasswordForm):
   new_password1 = forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplte': 'new-password','class':'form-control','placeholder':'Enter New Password' }), help_text= password_validation.password_validators_help_text_html())

   new_password2 = forms.CharField(label=_('New Confirm password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplte': 'new-password','class':'form-control','placeholder':'Enter confirm Password' }))


class ProfileForm(forms.ModelForm):
   class Meta:
      model = Customer
      fields = ['name', 'locality','city', 'zipcode', 'state' ]
      widgets = {
         'name': forms.TextInput(attrs={'class':'form-control'}),
         'locality' : forms.TextInput(attrs={'class':'form-control'}),
         'city' : forms.TextInput(attrs={'class':'form-control'}),
         'zipcode' : forms.NumberInput(attrs={'class':'form-control'}),
         'state' : forms.Select(attrs={'class':'form-control'})
      }