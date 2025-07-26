from django import forms
from .models import Profile
from. import models
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


class UserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email'
    ]

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Profile
        fields = ['bio','habite', 'img', 'slug']