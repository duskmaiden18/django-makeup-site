from django import forms
from .models import Care


class CareForm(forms.ModelForm):
    class Meta:
        model=Care
        fields = ['companies']
        widgets = {'companies': forms.Select(attrs={'class':'form-control'})}
