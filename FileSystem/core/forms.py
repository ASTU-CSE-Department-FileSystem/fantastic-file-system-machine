from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'description', 'category', 'reply', 'important']
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
