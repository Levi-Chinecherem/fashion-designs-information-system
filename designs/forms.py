# designs/forms.py
from django import forms
from .models import Design, Client
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class DesignForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Design
        fields = ['title', 'cover_image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Design Title'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['preferences']
        widgets = {
            'preferences': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Client Preferences'}),
        }
