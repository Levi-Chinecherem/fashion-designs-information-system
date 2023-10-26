from django import forms
from django.contrib.auth.models import User

GROUP_CHOICES = [
    ('clients', 'Clients'),
    ('designers', 'Designers'),
    ('both', 'Both'),
]

class UserCreationForm(forms.ModelForm):
    group = forms.ChoiceField(choices=GROUP_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'password', 'group']
