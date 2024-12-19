from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import ChecklistCreate
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.welcome, name='welcome'),
  path('home/', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('profile/', views.user_detail, name='user_detail'),
  path('edit/', views.edit_user, name='edit_user'),
  path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
  path('checklists/<int:checklist_id>/tasks/', views.get_checklist_tasks, name='get-checklist-tasks'),
  path('checklists/create/', views.ChecklistCreate.as_view(), name='checklist-create'),
  # path('checklists/', views.checklist_index, name='checklist-index'),#Do we need this?
  path('checklists/<int:checklist_id>/', views.checklist_detail, name='checklist-detail'),#do we need this?
  path('checklists/<int:pk>/update/', views.ChecklistUpdate.as_view(), name='checklist-update'),
  path('checklists/<int:pk>/delete/', views.ChecklistDelete.as_view(), name='checklist-delete'),
  path('checklists/<int:checklist_id>/add-task', views.add_task_to_checklist, name='add-task'),
  path('checklists/<int:checklist_id>/edit-task/<int:pk>/', views.ListitemUpdate.as_view(), name='edit-task'),
  path('checklists/<int:checklist_id>/delete-task/<int:pk>/', views.ListitemDelete.as_view(), name='delete-task'),
  path('reminders/', views.reminder_index, name='reminders-index'),
  path('checklists/<int:checklist_id>/new-reminder/<int:list_item_id>/', views.create_reminder, name='new-reminder'),
  path('reminders/<int:pk>/delete-reminder/', views.ReminderConfirmDeleteView.as_view(), name='delete-reminder'),
  path('checklists/<int:checklist_id>/share/', views.share_checklist, name='share-checklist'),
  path('deactivate/', views.deactivate_account, name='deactivate_account'),
  path('goodbye/', views.goodbye_page, name='goodbye'),
 ]