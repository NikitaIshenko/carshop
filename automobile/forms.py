from django import forms
from automobile.models import Automobile

class AutomobileForm(forms.ModelForm):

    class Meta:
        model = Automobile
        fields = '__all__'