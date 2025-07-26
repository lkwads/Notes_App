from django import forms
from .models import Notes
from ckeditor.widgets import CKEditorWidget


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'tags', 'img']