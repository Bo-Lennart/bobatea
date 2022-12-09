from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'

class ReserveTableForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput())
    class Meta:
        model = Reservation
        fields = '__all__'
