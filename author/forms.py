from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import re

class RegisterForm(forms.Form):

    username = forms.CharField(label='UserName')
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', str(username)):
            raise forms.ValidationError('Your UserName is not valid.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('This UserName is already taken!')

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(str(password)) < 8 :
            raise forms.ValidationError('Password must contain of at least 8 characters.')
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        email_re = re.compile(r'[^@]+@[^@]+\.[^@]+')
        if not re.search(email_re, email):
            raise forms.ValidationError('Please enter a valid e-mail address.')
        return email




class LoginForm(forms.Form):
    username = forms.CharField(label='UserName')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())





