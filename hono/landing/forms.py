from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import widgets

class AccountSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    field_order = ['first_name', 'last_name', 'email','username', 'password1', ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"       
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
