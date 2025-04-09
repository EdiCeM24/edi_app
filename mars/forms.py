from django import forms
from django.forms.widgets import PasswordInput, TextInput, Textarea
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'username', 'email', 'password1', 'password2']
        
        fname = forms.CharField(widgets=forms.TextInput())
        lname = forms.CharField(widget=forms.TextInput())
        username = forms.CharField(widget=forms.TextInput())
        email = forms.CharField(widget=forms.EmailInput())
        password1 = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    passWord = forms.CharField(widget=forms.PasswordInput())
    
    
class ContactForm(forms.Form):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
        
        fname = forms.CharField(widget=forms.TextInput())
        lname = forms.CharField(widget=forms.TextInput())
        email = forms.CharField(widget=forms.EmailInput())
        phone_number = PhoneNumberField(region='NG')
        subject = forms.CharField(widget=forms.TextInput())
        website = forms.CharField(widget=forms.URLField())
        company_name = forms.CharField(widget=forms.TextInput())
        message = forms.CharField(widget=forms.Textarea())  
        
            