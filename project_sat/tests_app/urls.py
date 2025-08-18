from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('analytics/', views.analytics_page, name='analytics'),
    path('projects/', views.projects_page, name='projects'),
    path('settings/', views.settings_page, name='settings'),
]
