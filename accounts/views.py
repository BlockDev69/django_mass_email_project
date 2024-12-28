from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages

from .forms import SignUpForm, LoginForm
from .tasks import send_welcome_email

USER = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Compte créé avec succès pour {user.username}!')
                send_welcome_email.delay(user.email)
                return redirect('reviews')
            else:
                messages.error(request, "Erreur lors de l'authentification après l'inscription.")
        else:
            messages.error(request, "Erreur dans le formulaire d'inscription")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('reviews')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
        else:
            messages.error(request, "Erreur dans le formulaire de connexion")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})