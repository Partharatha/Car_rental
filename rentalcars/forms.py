from django import forms
from rentalcars.models import cars

SEAT_CHOICES = [
    ('5', '5 seater'),
    ('7', '7 seater'),
]

class SeatFilterForm(forms.Form):
    seat = forms.ChoiceField(choices=[('', 'All')] + SEAT_CHOICES, required=False)
    company = forms.CharField(required=False)