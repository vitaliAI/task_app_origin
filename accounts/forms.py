from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """ Login Form """
    username = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Username",
                    }))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }))

    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = User.objects.filter(username=username).first()

        # Incorrect Password or Username
        if not user or not user.check_password(password):
            raise forms.ValidationError('Incorrect Username or Password')

        return self.cleaned_data


class RegistrationForm(forms.Form):
    """ Registration Form """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }))

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
            }))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }))

    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password Confirmation",
            }))

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        # Check if password has provided and also if confirmation matches
        if password and password != password_confirmation:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
