from django import forms
from django.contrib.auth.models import User
from user_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'autofocus': True}),
            "email": forms.TextInput(attrs={'placeholder': 'name@example.com'}),
        }


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'profile_pic')
