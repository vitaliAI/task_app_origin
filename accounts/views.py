from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegistrationForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Vitali in Development -> Redirect to Home View
                    return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'form': form})
    else:
        return render(request, 'accounts/login.html', {'form': LoginForm})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            User.objects.create_user(
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=request.POST.get('password')
            )
            return redirect('auth:login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        return render(request, 'accounts/register.html', {'form': RegistrationForm()})


def logout_view(request):
    logout(request)
    # Vitali in Development -> Redirect to Home View
    return redirect('home')