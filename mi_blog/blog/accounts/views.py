from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *
import os
from django.conf import settings


# Create your views here.

def register(request):    
    if request.method == 'POST':
        form = RegisterUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('LR')
        else:
            messages.error(request, 'No se a podido registrar ese usuario.')
            return redirect('../LR/#toregister')
    else:
        form= RegisterUserCreationForm()
        return render(request, 'accounts/login_register.html', {'form': form,})
    
@login_required
def logout_request(request):
    logout(request)
    return redirect('inicio')

    
def LR(request):
    return render(request,"accounts/login_register.html")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                return redirect('../LR/#tologin')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return redirect('../LR/#tologin')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_register.html', {'form': form})

@login_required
def edit_user(request):
    user = request.user
    try:
        avatar= Avatar.objects.get(user=user)
    except Avatar.DoesNotExist:
        avatar = None
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        avatar_form = AvatarForm(request.POST, request.FILES)
        password_form = CustomPasswordChangeForm(user, request.POST)
        if user_form.is_valid() and password_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            password_form.save()
            if avatar_form.cleaned_data.get('imagen'):
                if avatar:
                    avatar.imagen.delete()
                Avatar.objects.create(user=user, imagen=avatar_form.cleaned_data.get('imagen'))
            update_session_auth_hash(request, user)
            return redirect('../../appblog')
    else:
        user_form = UserEditForm(instance=user)
        avatar_form = AvatarForm()
        password_form = CustomPasswordChangeForm(user)
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'avatar_form': avatar_form,
        'password_form': password_form,
        'avatar': avatar.imagen.url if avatar else None,
    })


