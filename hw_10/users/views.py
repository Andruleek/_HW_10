from django.shortcuts import render, redirect
from .forms import AuthorForm
from .forms import RegisterForm
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
    else:
        form = AuthorForm()
    return render(request, 'users/create.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def home_view(request):
    return render(request, 'users/home.html')

def exit(request):
    return render(request, 'users/home.html')





