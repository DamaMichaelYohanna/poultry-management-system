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


def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
        else
        pass
    else:
        pass
    context = {}
    return render(request, 'add_user.html', context=context)


def change_password(request):
    pass


def recover_password(request):
    pass
