# from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login


class Signup(generic.FormView):
    """
    Signup view class
    """
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('articles:list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class Login(LoginView):
    """
    Login view class
    """
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    """
    logout view class
    """
    next_page = reverse_lazy('articles:list')
