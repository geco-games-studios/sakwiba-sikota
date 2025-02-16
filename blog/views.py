from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import BlogPost, Category
from django.views.generic import TemplateView

class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class WomenPageView(TemplateView):
    template_name = 'women.html'

class YouthPageView(TemplateView):
    template_name = 'youth.html'

class MinistriesPageView(TemplateView):
    template_name = 'ministries.html'
    