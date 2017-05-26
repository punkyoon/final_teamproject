from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'ID',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='username',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True',
            }
        )
    )
    
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    
    password2 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Password Confirm',
                'required': 'True',
            }
        ),
        help_text = "Enter the same password as above"
    )
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")