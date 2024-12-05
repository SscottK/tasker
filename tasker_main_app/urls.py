from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='welcome'),
  path('signup/', views.signup, name='signup'),
 ]