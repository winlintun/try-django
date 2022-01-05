from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        # if user is None:
        #     context = {"error": "Invalid username and password"}
        #     return render(request, 'account/login.html', context)
        # print(user)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
        context = {
            "form": form
        }
    return render(request, 'account/login.html', context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, 'account/logout.html', {})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'account/register.html', context)