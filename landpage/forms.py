from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=254, required=True, help_text='Required.')
    contact = forms.IntegerField(required=True, help_text='Required')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'contact' , )

class SignUpFormNGO(UserCreationForm):
    name = forms.CharField(max_length=30, required=True,help_text='*Required')
    email = forms.EmailField(max_length=254, required=True,help_text='*Required')
    address = forms.CharField(max_length=500,required=True,help_text='*Required')
    city = forms.CharField(max_length=40,required=True,help_text='*Required')
    pincode = forms.CharField(max_length=6,required=True,help_text='*Required')
    contact = forms.CharField(max_length=13, required=False,)
    #password
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2', 'address', 'city', 'pincode', 'contact' )
