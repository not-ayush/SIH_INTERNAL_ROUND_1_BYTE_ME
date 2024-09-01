from django import forms
from .models import share
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class shareform(forms.ModelForm):
    link = forms.URLField(
        max_length=200,
        widget=forms.URLInput(attrs={
            'placeholder': 'Please enter the link without .csv extension'
        }),
        help_text='Enter the URL without .csv extension'
    )

    class Meta:
        model = share
        fields = ['text', 'link', 'type_of_link']

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')