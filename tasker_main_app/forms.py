from django import forms
from .models import Checklist, Listitem, Reminder
from datetime import timedelta
from formset.widgets import DateTimePicker


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['list_name', 'status']


class ListitemForm(forms.ModelForm):
    class Meta:
        model = Listitem
        fields = ['step_name', 'description', 'high_priority', 'status']

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder_date']
        widgets = {
            'reminder_date': DateTimePicker(                
                attrs={                    
                    'step': timedelta(minutes=5)
                    
                }
            ),
        }