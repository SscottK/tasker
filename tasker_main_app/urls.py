from django.urls import path
from . import views
from .views import ChecklistCreate

urlpatterns = [
  path('', views.home, name='welcome'),
  path('signup/', views.signup, name='signup'),
 ]