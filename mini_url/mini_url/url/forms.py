from django import forms


class NouvelleURLForm(forms.Form):
    url = forms.CharField()
    pseudo = forms.CharField()
