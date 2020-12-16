from django import forms
from constructor.models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields =['first_name', 'last_name', 'fam_name']

        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'fam_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
