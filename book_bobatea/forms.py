from django import forms
from .models import Reservation
from django.db import models


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class ContactForm(forms.Form):
    name = models.CharField(max_length=50)
    name = models.IntegerField(max_length=50)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
