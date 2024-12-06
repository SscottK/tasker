from django.urls import path
from . import views
from .views import ChecklistCreate

urlpatterns = [
    path('', views.home, name='welcome'),
    path('checklists/create/', views.ChecklistCreate.as_view(), name='checklist-create'),
    path('checklists/', views.checklist_index, name='checklist-index'),
    path('checklists/<int:checklist_id>/', views.checklist_detail, name='checklist-detail'),
    path('checklists/<int:pk>/update/', views.ChecklistUpdate.as_view(), name='checklist-update'),
    path('checklists/<int:pk>/delete/', views.ChecklistDelete.as_view(), name='checklist-delete'),
    path('checklists/<int:checklist_id>/add-task', views.add_task_to_checklist, name='add-task'),
    path('checklists/<int:checklist_id>/edit-task/<int:pk>/', views.ListitemUpdate.as_view(), name='edit-task'),
    path('checklists/<int:checklist_id>/delete-task/<int:pk>/', views.ListitemDelete.as_view(), name='delete-task'),
    path('reminders/', views.reminder_index, name='reminder-index'),
    # path('checklists/<int:checklist_id>/new-reminder/<int:list_item_id>/', views.create_reminder, name='new-reminder'),
    path('checklists/<int:checklist_id>/new-reminder/<int:list_item_id>/', views.CreateReminderView.as_view(), name='new-reminder'),
]

