from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'base/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base/login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'base/register.html', {'error': error_message})
        
    return render(request, 'base/register.html')


def login(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'base/login.html', {'error': "Invalid credentials. Please try again."})
        
    return render(request, 'base/login.html')


@login_required
def dashboard(request):
    return render(request, 'base/dashboard.html', {'name': request.user.first_name})


@login_required
def videocall(request):
    return render(request, 'base/videocall.html', {'name': request.user.first_name + " " + request.user.last_name})


@login_required
def logouta(request):
    logout(request)
    return redirect('login')

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'base/join_room.html', {'name': request.user.first_name + " " + request.user.last_name})