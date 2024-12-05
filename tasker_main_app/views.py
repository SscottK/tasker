from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
#import reminder form

# Create your views here.


def home(request):
    return render(request, 'welcome.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # create a user form object
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # add  user to the database
            user = form.save()
            # log  user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


#create cron job to call mailer view
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