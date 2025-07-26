from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notes
from .forms import NoteForm 
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def all_notes(request):
    all_notes = Notes.objects.filter(user=request.user)
    context = {
        'all_notes' : all_notes
    }
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = request.POST.get('add_at')
        Contact.objects.create(name=name , email=email , phone=phone , message=message, add_at=date)
        messages.success(request, "your message envoyed")
    return render(request, 'notes.html', context)
def detail_note(request, slug):
    note = Notes.objects.get(slug=slug)
    if request.method == 'POST':
        try:
            print(" >>>>>>>>>>>> first if 1")
            note.delete()
            messages.success(request, "note was deleted succefuly")
            return redirect('/notes/')
        except:
            messages.error(request, "note is not found")
        
    context = {
        'note' : note
    }
    return render(request, 'detail_notes.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "completed!")
            return redirect('/notes')
        
    else:
        form = NoteForm()
    context = {
        'form' : form,
    }
    return render(request, 'add.html', context)

def edit(request, slug):
    note = get_object_or_404(Notes, slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            #new_form.user = request.user
            #new_form.save()
            messages.success(request, "edited")
            print("mission passed")
            return redirect(f'/notes/{slug}')
    else:
        form = NoteForm(instance=note)
    context = {
        'form' : form,
    }
    return render(request, 'edit.html', context)
from contact.models import Contact
