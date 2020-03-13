from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.forms import UserChangeForm
from accounts.forms import UserLoginForm, UserRegistrationForm, UserDetailsForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
# Create your views here.


def index(request):
    """Return the index.html file """
    return render(request, 'index.html')

@csrf_exempt
@login_required
def logout(request):
    """Log the user out """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))

@csrf_protect
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

    context = {
        "login_form": login_form
    }
    return render(request, 'login.html', context)

@csrf_protect
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

    context = {
        'registration_form': registration_form
    }
    return render(request, 'registration.html', context)


def user_profile(request):
    """ The users profile page """
    user = User.objects.get(email=request.user.email)
    userprofile = user.profile.objects.get(firstname=request.firstname,
                                           lastname=request.lastname,
                                           phone=request.phone,
                                           address=request.address,
                                           town=request.town,
                                           post_code=request.post_code,
                                           country=request.country,
                                           birth_date=request.birth_date
                                          )
    context = { 
        "profile": user,
        "userprofile": userprofile
    }
    return render(request, 'profile.html', context)

@csrf_protect
@login_required
@transaction.atomic
def edit_profile(request, pk):

    user = User.objects.get(pk=id)
    if request.method == 'POST':
        profile_form = UserDetailsForm(request.POST, instance=request.profile.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            user.save()
            messages.success('Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error('Please correct the error below.')
    else:
        profile_form = UserDetailsForm(instance=request.profile.userprofile)
    
    context = {
        'profile_form': profile_form
    }
    return render(request, 'userdetails.html', context)


def fucking_views(request):
    profile_form = UserDetailsForm(instance=request.user.userprofile)
    return render(request, 'userdetails.html', {
        'profile_form': profile_form
    })
