from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    if request.user.is_authenticated :
        return redirect('/notes/')
    else:
        return redirect('/login/')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usr = authenticate(username=username, password=password)
            if usr is not None:
                LoginView(request , usr)
                messages.success(request, "sign up completed succefuly")
                return redirect('/notes')
    else:
        form = UserCreationForm()

    
    context = {
        'form':form ,
    }
    return render(request , 'sign.html', context)
