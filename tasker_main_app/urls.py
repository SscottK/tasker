from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import ChecklistCreate

urlpatterns = [
  path('', views.home, name='welcome'),
  path('signup/', views.signup, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
 ]