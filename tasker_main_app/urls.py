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

]