from django.shortcuts import render
from auth import forms
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView

def login(request):
    error = None
    form = forms.LoginForm()
    if request.method=='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = "INVALID USERNAME OR PWD"

    context = {
        "form" : form,
        "error" : error
    }
    return render(request, 'login.html', context)

class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    pass