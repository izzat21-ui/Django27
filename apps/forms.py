from typing import re

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from apps.models import todo_lists, Cars, Wallet, User







class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = 'password', 'email', 'phone'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone')
        pattern = "^\+998?:33|55|77|88|90|91|93|94|95|97|98|99\d{7}$"
        if not re.match(pattern, phone_number):
            raise ValidationError('Phone number must be entered in the format: ')
        return phone_number


class UserForm(Form):
    class Meta:
        model = User
        fields = 'email', 'password'



