from django import forms
from myapp.models import Patient


class PatientForm(forms.ModelForm):

    info = forms.CharField(widget=forms.Textarea())

    class Meta():
        model = Patient
        fields = '__all__'