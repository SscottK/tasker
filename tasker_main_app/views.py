from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Checklist
from .forms import ChecklistForm

# Create your views here.

def home(request):
    return render(request, 'welcome.html')

#checklist create view
class ChecklistCreate(CreateView):
    model = Checklist
    form_class = ChecklistForm
    template_name = 'main_app/checklist_form.html'
    success_url = '/checklists/checklist_id'

#view of all checklists
def checklist_index(request):
    checklists = Checklist.objects.all()

    return render(request, 'checklists/index.html', {'checklists': checklists})


#view of one checklist
def checklist_detail(request, checklist_id):
    checklist = get_object_or_404(Checklist, id=checklist_id)

    return render(request, 'checklists/detail.html', {
        'checklist': checklist,
    })


#edit checklist
class ChecklistUpdate(UpdateView):
    model = Checklist
    fields = ['list_name', 'status']

#delete checklist
class ChecklistDelete(DeleteView):
    model = Checklist
    success_url = '/checklists/'