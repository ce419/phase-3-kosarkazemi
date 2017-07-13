from django import forms
from django.core.exceptions import ObjectDoesNotExist
import re
from .models import User , Blog


class RegisterForm(forms.Form):


    std_num = forms.IntegerField(label='Student Number', max_length=10)
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')
