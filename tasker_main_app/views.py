
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Checklist, Listitem
from .forms import ChecklistForm, ListitemForm

# Create your views here.

def home(request):
    return render(request, 'welcome.html')

#checklist create view
class ChecklistCreate(CreateView):
    model = Checklist
    form_class = ChecklistForm
    template_name = 'main_app/checklist_form.html'
    #success_url = '/checklists/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('checklist-index')

#view of all checklists
def checklist_index(request):
    checklists = Checklist.objects.filter(owner=request.user)

    return render(request, 'checklists/index.html', {'checklists': checklists})


#view of one checklist
def checklist_detail(request, checklist_id):
    checklist = get_object_or_404(Checklist, id=checklist_id)
    listitems = checklist.listitem_set.all()

    return render(request, 'checklists/detail.html', {
        'checklist': checklist,
        'listitems': listitems,
    })


#edit checklist
class ChecklistUpdate(UpdateView):
    model = Checklist
    fields = ['list_name', 'status']
    template_name = 'main_app/checklist_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('checklist-detail', kwargs={'checklist_id': self.object.id})

#delete checklist
class ChecklistDelete(DeleteView):
    model = Checklist
    success_url = '/checklists/'
    template_name = 'main_app/checklist_confirm_delete.html'


def add_task_to_checklist(request, checklist_id):
    checklist = get_object_or_404(Checklist, id=checklist_id)

    if request.method == 'POST':
        form = ListitemForm(request.POST)
        if form.is_valid():
            listitem = form.save(commit=False)
            listitem.checklist = checklist
            listitem.save
            return redirect('checklist-detail', checklist_id=checklist.id)
    else:
        form = ListitemForm()

    return render(request, 'checklists/add_task.html', {
        'form': form,
        'checklist': checklist,
    })    

class ListitemUpdate(UpdateView):
    model = Listitem
    form_class = ListitemForm
    template_name = 'checklists/edit_task.html'

    def get_success_url(self):
        checklist_id = self.object.checklist.id
        return reverse_lazy('checklist-detail', kwargs={'checklist_id': checklist_id})


#mailer
#try
#get all reminders that need to be sent out in the next 30 mins
#for all reminders
#if reminder has not been sent
#send reminder
#mark reminder as sent
#when done reply with ok it worked
#except
#if an error occurs reply with error


#Create reminder view
#define create reaminder args. request, user_id, list_item_id
#assign reminder form request to form variable
#check to see if form is_valid()
    #create new reminder variable but do not save anything to it
    #new reminder = form.save(commit=false)
    #Add user_id to new reminder
    #Add list_item_id to new reminder
    #save new reminder
#redirect to list detail




#Edit reminder view

#reminders index view

#Delete reminder view