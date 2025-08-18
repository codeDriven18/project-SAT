from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def main_page(request):
    return render(request, 'home.html')

@login_required
def analytics_page(request):
    return render(request, 'analytics.html')

@login_required
def projects_page(request):
    return render(request, 'projects.html')

@login_required
def settings_page(request):
    if request.method == "POST":
        request.user.full_name = request.POST.get("full_name", request.user.full_name)
        request.user.email = request.POST.get("email", request.user.email)
        request.user.save()
        return redirect('settings')
    return render(request, 'settings.html')
