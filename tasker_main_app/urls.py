from django.urls import path
from . import views
from .views import ChecklistCreate

urlpatterns = [
    path('', views.home, name='home'),
    path('checklists/create/', views.ChecklistCreate.as_view(), name='checklist-create'),
    path('checklists/', views.checklist_index, name='checklist-index'),
]