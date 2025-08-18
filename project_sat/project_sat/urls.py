# C:\proggggg\project-SAT\project_sat\project_sat\urls.py
from django.contrib import admin
from django.urls import path, include
from tests_app.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('accounts/', include('accounts.urls')),  # login/logout
]
