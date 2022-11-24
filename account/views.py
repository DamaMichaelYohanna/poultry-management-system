from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

from account.forms import UserForm, ProfileForm
from account.models import Profile


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            error = True
            return render(request, "login.html", {'status': error})
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user.id)
    all_profile = Profile.objects.all()
    print(user_profile)
    context = {'user_profile': user_profile, "all_users": all_profile}
    return render(request, 'profile.html', context)


@login_required
def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()

    else:
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
    context = {'user': user_form, 'profile': profile_form}
    return render(request, 'add_user.html', context=context)


@login_required
def update_profile(request, pk):
    info = Profile.objects.get(pk=pk)
    acc = User.objects.get(profile=info)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=acc)
        profile_form = ProfileForm(request.POST, request.FILES, instance=info)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # profile_form.save(commit=False)
            profile_form.save()
            return redirect(reverse("account:profile"))
    else:
        user_form = UserForm(instance=acc)
        profile_form = ProfileForm(instance=info)
    context = {'user': user_form, 'profile': profile_form}
    return render(request, 'update_profile.html', context)


@login_required
def delete_profile(request, pk):
    info = Profile.objects.get(pk=pk)
    acc = User.objects.get(profile=info)
    if request.user.is_superuser:
        # del info
        # del acc
        pass

    return redirect(reverse('account:profile'))


def change_password(request):
    pass


def recover_password(request):
    pass


