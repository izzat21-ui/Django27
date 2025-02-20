from typing import re

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from apps.models import todo_lists, Cars, Wallet, User


class TododelView(ModelForm):
    class Meta:
        model = todo_lists  # ✅ Vergul olib tashlandi
        fields = ['title']


class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['name', 'price', 'speed', 'km']


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


class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = 'amount', 'category', 'description'

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        return amount.strip('$')


class UserForm(Form):
    class Meta:
        model = User
        fields = 'email', 'password'


class HomeForm(ModelForm):
    class Meta:
        model = User
        fields = 'email', 'password'


class SahifaForm(ModelForm):
    class Meta:
        model = User
        fields = 'email', 'password'
    # def is_authenticated(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     user = User.objects.filter(email=email)
