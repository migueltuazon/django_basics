form django import forms

form .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'note',
        )