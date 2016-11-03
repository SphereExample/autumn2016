from django import forms
from space.models import Planet

class PlanetForm(forms.ModelForm):
    
    class Meta:
        model = Planet
        exclude = ()
