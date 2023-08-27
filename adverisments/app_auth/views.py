from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreationUserForm


def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error': '404 User not found'})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def profile_view(request):
    return render(request, 'app_auth/profile.html')


def register_view(request):
    redirect_url = reverse('profile')
    if request.method == 'POST':
        form = CreationUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                return redirect(redirect_url)
            url = reverse('register')
            return redirect(url)
    else:
        form = CreationUserForm()

    context = {'form': form}
    return render(request, 'app_auth/register.html', context)
