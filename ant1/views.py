from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ant1.forms import LoginForm, PersonneProfileForm
from ant1.models import Personne

def get_logger_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        return Personne.objects.get(id=logged_user_id)
    else:
        return None


def welcome(request):
    logged_user = get_logger_user_from_request(request)
    if logged_user:
        return render(request, "welcome.html", {'logged_user': logged_user})
    else:
        return render(request, "welcome.html")


def login(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            logged_user = Personne.objects.get(email=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect('/welcome')
        else :
            return render(request, 'login.html', {'form': form})
    else :
        form = LoginForm()
        return render(request, "login.html", {"form": form})

def logout(request):
    try:
        del request.session['logged_user_id']
    except KeyError:
        pass
    return redirect('/welcome')

def register(request):
    if len(request.POST) > 0:
        form = PersonneProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, 'user_profile.html', {'form': form})
    else:
        form = PersonneProfileForm()
        return render(request, 'user_profile.html', {'form': form})

def modify_profile(request):
    logged_user = get_logger_user_from_request(request)
    if logged_user:
        if len(request.POST) > 0:
            form = PersonneProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/welcome')
            else:
                return render(request, 'modify_profile.html', {'form': form, 'logged_user': logged_user})
        else:
            form = PersonneProfileForm(instance=logged_user)
            return render(request, 'modify_profile.html', {'form': form, 'logged_user': logged_user})
    else:
        return redirect('/login')

def option1(request):
    logged_user = get_logger_user_from_request(request)
    if logged_user:
        return render(request, "option1.html", {'logged_user': logged_user})
    else:
        return render(request, "welcome.html")