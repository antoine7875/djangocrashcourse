from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ant1.forms import LoginForm


def welcome(request):
    return render(request, "welcome.html")


def login(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/welcome')
        else :
            return render(request, 'login.html', {'form': form})
    else :
        form = LoginForm()
        return render(request, "login.html", {"form": form})

def register(request):
    return render(request, "register.html")