from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Checklist
from .forms import ChecklistForm

# Create your views here.

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

class ChecklistCreate(CreateView):
    model = Checklist
    form_class = ChecklistForm
    template_name = 'main_app/checklist_form.html'
    success_url = '/checklists/'


def checklist_index(request):
    checklists = Checklist.objects.all()

    return render(request, 'checklists/index.html', {'checklists': checklists})