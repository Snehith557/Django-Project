
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls') ),
    path('projects/',include('projects.urls')),
    path('feedback/',include('feedback.urls')),
]
