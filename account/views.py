from django.shortcuts import render , redirect
from django.contrib.auth import  authenticate
from django.contrib.auth.views import LoginView 
from .models import Profile 
from django.shortcuts import get_object_or_404
from .forms import ProfileForm , UserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from notes_app.models import Notes
# Create your views here.
def home(request):
    pass

def profiel(request, slug):    
    form = Profile.objects.get(slug=slug)
    context = {'form': form}
    return render(request, 'profile.html', context)

def edit(request, slug):
    profiel= get_object_or_404(Profile ,slug=slug)
    if request.method == 'POST' and 'save' in request.POST :
        print("<<<<<<<<<<<<<<<< passed")
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES , instance=profiel)
        print("user_form errors:", user_form.errors)
        print("profile_form errors:", profile_form.errors)
        print("POST data:", request.POST)
        print('passed1')
        if profile_form.is_valid()  and user_form.is_valid():
            print('passed2')
            user_form.save()
            new_form = profile_form.save(commit=False)
            new_form.save()
            messages.success(request, "Profile was updated succefuly.")
            return redirect('/notes/')
    elif request.method == 'POST' and 'delete' in request.POST :
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES , instance=profiel)
        try:
            profiel.user.delete()
            messages.success(request, "account was deleted succefuly!")
            return redirect('/')
        except:
            messages.error(request, "enable to delte your account!")

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profiel)

    context = {
        'user_form' : user_form,
        'profile_form':profile_form,
    }
    return render(request, 'edit_profile.html' ,context)

def change_password(request , slug) :
    profiel = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "password changing succefuly.")
            return redirect('/notes/')
        else:
            messages.error(request, "password incorrect")

    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form ,
        }
    
    return render(request , 'change.html', context)