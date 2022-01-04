from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username and password"}
            return render(request, 'account/login.html', context)
        print(user)
        login(request, user)
        return redirect("/")
    return render(request, 'account/login.html', {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, 'account/logout.html', {})


def register_view(request):
    return render(request, 'account/login.html', {})