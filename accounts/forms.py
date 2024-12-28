from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Nom',
        min_length=4,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Nom d'utilisateur",
            'id': 'username'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'E-mail',
            'id': 'email'
        })
    )
    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Saisir mot de passe',
            'id': 'password1'
        })
    )
    password2 = forms.CharField(
        label='Confirmation',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Confirmer mot de passe',
            'id': 'password2'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Nom d'utilisateu",
            'id': 'username'
        })
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Mot de passe',
            'id': 'password'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password')