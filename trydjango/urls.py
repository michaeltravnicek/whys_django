"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from products.views import (
    home_view, 
    ImportView,
    ModelDetailView,
    ModelListView,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    
    # Get
    path('detail/<str:model_name>/', ModelListView.as_view(), name='list all records for model'),
    path('detail/<str:model_name>/<int:id>', ModelDetailView.as_view(), name='all data for one record'),

    # Post 
    path('import/', ImportView.as_view(), name='import-list-entities'),
]
