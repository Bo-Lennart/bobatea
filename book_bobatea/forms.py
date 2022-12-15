from django import forms
from .models import Reservation, TeaMenu


class ReserveTableForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'time': forms.TimeInput(attrs={'type':'time', 'min': '12:00'}),
        }


class add_item_to_menu_form(forms.ModelForm):

    class Meta:
        model = TeaMenu
        fields = '__all__'