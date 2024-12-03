from django import forms
from .models import Checklist, Listitem


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['list_name', 'status', 'owner']


class ListitemForm(forms.ModelForm):
    class Meta:
        model = Listitem
        fields = ['step_name', 'description', 'high_priority', 'status']