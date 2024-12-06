from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#The status of a Whole list or a single list item
STATUS_CHOICES = (
    ('N', 'Not Started'),
    ('I', 'In Progress'),
    ('C', 'Complete'),
)

#Checklist model
class Checklist(models.Model):
    #Name of the Cheklist
    list_name = models.CharField(max_length=50)
    #Status of the Checklist
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0]
    )
    #The owner of the Checklist
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    #Keeping track or creation and updates date and time (to implement leaderboard feature later)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #changing string method to display object name when printing the object to console
    def __str__(self):
        return self.list_name

#List item model
class Listitem(models.Model):
    #Step name
    step_name = models.CharField(max_length=50)
    #A descriptopn of how to complete the step
    description = models.TextField(max_length=1000)
    #list item priority
    high_priority = models.BooleanField(default=False)
    #List item status
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0],
    )
    #checlist the list item belongs to
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    #keeping trak of date and time for reminders
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #changing string method to display object name when printing the object to console
    def __str__(self):
        return self.step_name

#roles to be assigned when adding users to a checklist
ROLE_CHOICES = (
    ('R', 'Read Only'),
    ('E', 'Editor'),
)


#Assigning a role to a user that is not the owner of the list
class List_user(models.Model):
    #The user being assigned a role
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #The role being assigned to the user
    role = models.CharField(
        max_length=1,
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0],
    )
    #The Checklist to which the user is being assigned a role for
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    #changing string method to display object name when printing the object to console
    def __str__(self):
        return self.user

#Reminders for list items
class Reminder(models.Model):
    #List item the reminder belongs to
    list_item =  models.ForeignKey(Listitem, on_delete=models.CASCADE)
    #the day the reminder should be sent
    reminder_date = models.DateTimeField()
    #reminder sent or not as to not repeat reminders
    reminder_sent = models.BooleanField(default=False)
    #The User who created the reminder
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #changing string method to display object name when printing the object to console
    def __str__(self):
        return self.user