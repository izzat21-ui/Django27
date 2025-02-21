from django.test import TestCase

# Create your tests here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import  ListView, FormView,

from apps.forms import RegisterModelForm, UserForm,  SahifaForm
from apps.models import  User



class RegisterFormView(FormView):
    template_name = 'User/register.html'
    form_class = RegisterModelForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        for message in form.errors:
            messages.error(self.request, message)
        return super().form_invalid(form)



class IncomeFormView(FormView, ListView):
    queryset = Category.objects.filter(type=Category.Type.INCOME)
    form_class = WalletForm
    template_name = 'User/../templates/income.html'
    success_url = reverse_lazy('home_page')
    context_object_name = "categories"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    template_name = 'User/login.html'
    form_class = UserForm
    success_url = reverse_lazy('login-html')


class HomeFormView(FormView):
    template_name = 'User/user.html'
    form_class = UserForm
    success_url = reverse_lazy('user')



