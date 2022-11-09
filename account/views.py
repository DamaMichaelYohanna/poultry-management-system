from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username, password)
        if user:
            login(request, user)
        return redirect('/')
    else:
        return render(request, "account/login.html")

def logout_view(request):
    logout(request)
    return redirect('/')