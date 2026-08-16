from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render,redirect


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

from django.contrib.auth import login

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('/')
        else:
            form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')