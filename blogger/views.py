from django.shortcuts import render
from .models import LatestNews, BlogInsights

def home(request):
    news = LatestNews.objects.all().order_by('-created_at')[:3]
    insights = BlogInsights.objects.all().order_by('-created_at')[:4]
    return render(request, 'index.html', {'news': news, 'insights': insights})

def about(request):
    return render(request, 'about.html')

def experience(request):
    return render(request, 'experience.html')

def works(request):
    return render(request, 'works.html')

def insights(request):
    return render(request, 'insights.html')

def contact(request):
    return render(request, 'contact.html')

def stories(request):
    return render(request, 'stories.html')