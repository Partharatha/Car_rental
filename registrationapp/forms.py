from django import forms
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from registrationapp.models import UserRegistration


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['phone','door_no','street','landmark','city','state','zip_code','userpic']
    captcha = ReCaptchaField()
    

class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']    

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['phone','door_no','street','landmark','city','state','zip_code','userpic']


#! paasword reset 

class PasswordResetForm(forms.Form):
    Username = forms.CharField(max_length=100)
    New_Password = forms.CharField(max_length=100)
    Confirm_New_Password = forms.CharField(max_length=100,widget=forms.PasswordInput())

 