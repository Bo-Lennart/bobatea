from django import forms
from .models import Reservation, TeaMenu, CancelReservation


class ReserveTableForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'min': '', 'max': ''}),
            'time': forms.TimeInput(attrs={'type': 'time', 'min': '12:00', 'max': '21:00'}),
        }


class add_item_to_menu_form(forms.ModelForm):

    class Meta:
        model = TeaMenu
        fields = '__all__'


class CancelReservationForm(forms.ModelForm):

    class Meta:
        model = CancelReservation
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'min': '', 'max': ''}),
            'time': forms.TimeInput(attrs={'type': 'time', 'min': '12:00', 'max': '21:00'}),
        }
