from django import forms
from django.core.exceptions import ObjectDoesNotExist
import re
from .models import User , Blog


class RegisterForm(forms.Form):

    std_num = forms.IntegerField(label='Student Number')
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean_std_num(self):
        std_num = self.cleaned_data['std_num']
        if not re.search(r'^\d+$', std_num):
            raise forms.ValidationError('Your Student Number is not valid')
        try:
            User.objects.get(std_num=std_num)
        except ObjectDoesNotExist:
            return std_num
        raise forms.ValidationError('This Student already has an account!')

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8 :
            raise forms.ValidationError("Password must contain of at least 8 characters")
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        email_re = re.compile(
            r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
            r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
            r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain
        if not re.search(email_re, email):
            raise forms.ValidationError('Please enter a valid e-mail address.')





class LoginForm(forms.Form):
    std_num = forms.IntegerField(label='Student Number')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

