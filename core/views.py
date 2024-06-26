from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from django.http import HttpResponse


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('core:home')
            else:
                return HttpResponse('Invalid username or password. Please try again letter.')

    else:
        form = LoginForm()
    return render(request, 'core/login.html', {
        'form': form
    })


def user_registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # Enable password hashing first
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('core:login')
    else:
        user_form = RegistrationForm()

    return render(request, 'core/register.html', {
        'user_form': user_form
    })


@login_required
def home(request):
    return render(request, 'core/home.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('core:login')
