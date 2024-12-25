from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['category', 'weight', 'video']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'video': forms.URLInput(attrs={'class': 'form-control'}),
        }