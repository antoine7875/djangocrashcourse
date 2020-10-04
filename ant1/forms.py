# -*- coding: utf-8 -*-

from django import forms
from ant1.models import Personne

class LoginForm(forms.Form):
  email = forms.EmailField(label='Courriel :')
  motdepasse = forms.CharField(label='Mot de passe :', widget = forms.PasswordInput)
  def clean(self):
    cleaned_data = super(LoginForm, self).clean()
    email = cleaned_data.get("email")
    motdepasse = cleaned_data.get("motdepasse")
    
    # Vérifie que les deux champs sont valides
    if email and motdepasse:
      result = Personne.objects.filter(motdepasse=motdepasse, email=email)
      if len(result) !=1:
        raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")
    return cleaned_data

class PersonneProfileForm(forms.ModelForm):
  class Meta:
    model = Personne
    fields = ['prenom', 'nom', 'email', 'motdepasse']