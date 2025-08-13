from django.shortcuts import render

def quiz_view(request):
    return render(request, 'tests_app/quiz.html')
