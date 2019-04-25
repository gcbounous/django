from django import forms
from .models import MiniURL


class NouvelleURLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ('url', 'pseudo')
