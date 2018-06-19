import sys
from django.shortcuts import render
from user_app.forms import UserForm, UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request, 'user_app/index.html')


def register(request):

    registered = False
    if request.method == 'POST':
        try:
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)
        except Exception as e:
            raise AttributeError("UserProfileInfoForm has no 'request' attribute")

        try:
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']

                profile.save()

                registered = True
        except:
            raise OSError(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])

        else:
            user_form = UserForm
            profile_form = UserProfileInfoForm

        cntx = {'user_form' : user_form,
                'profile_form' : profile_form,
                'registered' : registered}
        return render(request, 'user_app/registration.html', context=cntx)
    else:
        user_form = UserForm
        profile_form = UserProfileInfoForm
        cntx = {'user_form' : user_form,
                'profile_form' : profile_form,
                'registered' : registered}
        return render(request, 'user_app/registration.html', context=cntx)


