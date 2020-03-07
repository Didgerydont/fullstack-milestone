from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.forms import UserLoginForm, UserRegistrationForm, UserDetailsForm
from django.db import transaction
# Create your views here.


def index(request):
    """Return the index.html file """
    return render(request, 'index.html')


@login_required
def logout(request):
    """Log the user out """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))


def login(request):
    """ Return a login page """
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """ render the registration page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")

    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
                  {'registration_form': registration_form})


def user_profile(request):
    """ The users profile page """
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})


@login_required
@transaction.atomic
def edit_profile(request, user_id):
    if request.method == 'POST':
        profile_form = UserDetailsForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success('Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error('Please correct the error below.')
    else:
        profile_form = UserDetailsForm(instance=request.user.Profile)
    return render(request, 'userdetails.html', {
        'profile_form': profile_form
    })

def fucking_views(request):
    return render(request, 'userdetails.html')
