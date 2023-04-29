from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from blog_app.forms import *
from .models import *
from .forms import *

def inicio(request):
    return render(request,"blog_app/index.html")

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
                return render(request, 'blog_app/login.html', {'form': form, 'mensaje': 'Usuario o contraseña incorrectos.'})
        else:
                return render(request, 'blog_app/login.html', {'form': form, 'mensaje': 'Usuario o contraseña incorrectos.'})
    else:
        form = AuthenticationForm()
    return render(request, 'blog_app/login.html', {'form': form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = RegisterUserCreationForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return redirect('../')

    else:

        miFormulario = RegisterUserCreationForm(initial={'email': usuario.email})

    return render(request, "blog_app/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

def register(request):
    if request.method == 'POST':
        form = RegisterUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('../login')
        else:
            return render(request, 'blog_app/register.html', {'form': form, "mensaje":"Error al crear usuario"})
    else:
        form= RegisterUserCreationForm()
        return render(request, 'blog_app/register.html', {'form': form,})

@login_required
def logout_request(request):
    logout(request)
    return redirect('inicio')

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()

            # Save the new password
            password_form.save()
            update_session_auth_hash(request, request.user)

            return redirect('inicio')
    else:
        user_form = UserEditForm(instance=user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'blog_app/editarPerfil.html', {
        'user_form': user_form,
        'password_form': password_form,
        'user': user,
    })