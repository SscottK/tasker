from django import forms
from .models import Checklist, Listitem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['list_name', 'status']


class ListitemForm(forms.ModelForm):
    class Meta:
        model = Listitem
        fields = ['step_name', 'description', 'high_priority', 'status']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']