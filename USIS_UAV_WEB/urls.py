"""
Definition of urls for USIS_UAV_WEB.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('uav_overview', include('uav_overview.urls')),
    path('uav_drawings_design', include('uav_drawings_design.urls')),
    path('uav_project_basics', include('uav_project_basics.urls')),
    path('uav_project_lifecycle', include('uav_project_lifecycle.urls')),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
