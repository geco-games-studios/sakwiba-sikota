from django.shortcuts import render
from .models import LatestNews, BlogInsights

def home(request):
    context = {
        'is_home': True,  # Indicates this is the home page
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def experience(request):
    return render(request, 'experience.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def insights(request):
    return render(request, 'insights.html')

def contact(request):
    return render(request, 'contact.html')

def stories(request):
    return render(request, 'stories.html')