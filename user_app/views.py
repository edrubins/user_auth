import sys
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from user_app.models import UserProfileInfo
from user_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'user_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        if not next:
            next = reverse('index')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active.")
        else:
            print("Login Falied!")
            print("Username: {} Password {}".format(username, password))
            return HttpResponse("Invalid login atttempted.")

    return render(request, 'user_app/login.html')

@login_required
def user_list(request):
    profiles = UserProfileInfo.objects.all()

    return render(request, 'user_app/user_list.html', context={'profiles' : profiles, 'row_classes' : {'odd': 'odd_row', 'even' : 'even_row'}} )

def handler404(request):
    # response = render_to_response('404.html', {}, context_instance = RequestContext(request))
    # response.status_code = 404

    get = request.GET
    for item in get.keys():
        print("{}: {}".format(item, get[item]))

    return render(request, 'user_app/404.html', context=request)

def handler500(request):
    # response = render_to_response('500.html', {}, context_instance = RequestContext(request))
    # response.status_code = 500

    get = request.GET
    print("response.GET:")
    for item in get.keys():
        print("{}: {}".format(item, get[item]))

    return render(request, 'user_app/500.html', context={})

