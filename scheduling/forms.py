# scheduling/forms.py
from django import forms
from .models import Appointment, ContactMessage
from django.contrib.auth.models import User

class AppointmentForm(forms.ModelForm):
    designer = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='Designer'),
        empty_label="Select a designer"
    )

    class Meta:
        model = Appointment
        fields = ['designer', 'date', 'start_time', 'end_time', 'status', 'description']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select a date'})
        self.fields['start_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Set start time'})
        self.fields['end_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Set end time'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a description'})
        self.fields['designer'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }
