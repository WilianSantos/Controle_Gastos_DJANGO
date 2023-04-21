from django import forms

from .models import Rendas


class AdicionarRenda(forms.ModelForm):
    class Meta:
        model = Rendas
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()
    