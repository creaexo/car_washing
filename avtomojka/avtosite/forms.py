from django import forms
from .models import *


class Zapis(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['Phone', 'Number', 'Wash', 'Salon', 'Avto', 'Time', 'HydroShine']
        widgets = {
            'Phone': forms.TextInput(attrs={'name': 'tel', 'placeholder': '+7 (999) 999 99 99', 'id': 'tel', 'required': ''}),
            'Number': forms.TextInput(attrs={'name': 'nomer', 'placeholder': 'Н798УХ196', 'id': 'nomer'}),
            'Avto': forms.Select(attrs={'name': 'avto', 'id': 'avto'}),
            'Salon': forms.Select(attrs={'name': 'salon', 'id': 'salon'}),
            'Time': forms.Select(attrs={'name': 'time', 'id': 'time'}),
            'HydroShine': forms.CheckboxInput(attrs={'class': 'pere'}),

        }
