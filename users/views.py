from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from django.contrib.auth import login as log_in
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            log_in(request, user)
            messages.success(request, f"Inscription effectuée avec succès !")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'title': "Inscription",
        'header_title': "Inscription", })


def profile(request):

    return render(request, 'users/profil.html', {'title': "Page de profil",})



def logout(request):
    log_out(request)
    messages.info(request, "On espere vous revoir bientot !")
    return redirect("core:home")


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                log_in(request, user)
                messages.info(request, f"Bienvenue {username} !")
                return redirect('/')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})