from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Simple test view for root URL
def home(request):
    return render(request, 'index.html')  # This will render the default Django homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Route for '/'
]