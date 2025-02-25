from django.contrib import admin
from django.urls import path
from blogger import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('insights/', views.insights, name='insights'),
    path('stories/', views.stories, name='stories'),
    path('contact/', views.contact, name='contact'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)