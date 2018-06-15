from django.shortcuts import render
from user_app.forms import UserProfile, UserForm
# Create your views here.
def index(response):
    return render(response, 'user_app/index.html')

def register(response):
    user_form = UserForm
    profile_form = UserProfile
    return render(response, 'user_app/registration.html', context={'registered' : False, 'user_form' : user_form, 'profile_form' : profile_form})


