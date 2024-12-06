"""
URL configuration for tasker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasker_main_app.urls')),
    path(
        'jsi18n/',
        cache_page(3600)(JavaScriptCatalog.as_view(packages=['formset'])),
        name='javascript-catalog'
    )
]
