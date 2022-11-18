from django.contrib.auth import login, get_user_model, logout, authenticate
from django.shortcuts import render, redirect

User = get_user_model()


def signup(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, password=password)

        login(request, user)

        return redirect('index')

    return render(request, 'accounts/signup.html')


# login_user
def login_user(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html')


# logout_user
def logout_user(request):
    logout(request)

    return redirect('index')


# profile
def profile(request):
    user = request.user

    return render(request, 'accounts/profile.html', {'user': user})


def update_profile(request):
    if request.method == 'POST':
        # traiter le formulaire
        user = request.user
        user.username = request.POST.get('username')
        user.last_name = request.POST.get('last_name')
        user.first_name = request.POST.get('first_name')
        user.save()
        return redirect('profile')

    return render(request, 'accounts/update-profile.html')
