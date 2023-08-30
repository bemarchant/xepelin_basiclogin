from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        # form = UserLoginForm(request.POST), this will not work
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('welcome')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('welcome')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    
    form = NewUserForm()
    return render(request, 'signup.html', context={'form': form})

@login_required

def user_logout(request):
    return redirect('user_login')

def welcome(request):
    return render(request, 'welcome.html')