from django.urls import path
from .views import HomePageView, BlogPostDetailView, AboutPageView, WomenPageView, YouthPageView, MinistriesPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('women/', WomenPageView.as_view(), name='women'),
    path('youth/', YouthPageView.as_view(), name='youth'),
    path('ministries/', MinistriesPageView.as_view(), name='ministries'),
]