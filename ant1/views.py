from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ant1.forms import LoginForm


def welcome(request):
    return render(request, "welcome.html")


def login(request):
  # Test si formulaire a été envoyé
  if len(request.POST) > 0:
    # Test si les paramètres attendus ont été transmis
    if 'email' not in request.POST or 'password' not in request.POST:
      error = "Veuillez entrer une adresse de courriel et un mot de passe."
      return render(request, "login.html", {'error': error})
    else:
      email = request.POST['email']
      password = request.POST['password']
      # Testrequest  si le mot de passe est le bon
      if password != 'sesame' or email != 'pierre@lxs.be':
        error = "Adresse de courriel ou mot de passe erroné."
        return render(request, "login.html", {'error': error})      
      # Tout est bon, on va à la page d'accueil
      else:
        return redirect("/welcome")
  # Le formulaire n'a pas été envoyé
  else:
    return render (request, "login.html")

def register(request):
    return render(request, "register.html")