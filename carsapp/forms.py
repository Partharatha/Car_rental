from django import forms
from carsapp.models import Products,Bookdrive
from carsapp.models import Enquiry

class ProductEmiForm(forms.ModelForm):
    product_name=forms.CharField(disabled=True)
    price=forms.CharField(disabled=True)
    class Meta:
        model=Products
        fields=['product_name','price']
    loan_amount=forms.IntegerField()
    tensure=forms.IntegerField()
class BookDriveForm(forms.ModelForm):
    class Meta:
        model = Bookdrive
        fields = ['date', 'timings','phone']
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['phone', 'consern']            