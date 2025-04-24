"""
URL configuration for newComm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

# Define a simple health check view
def ping_view(request):
    """A simple view that returns 'pong'."""
    return HttpResponse("pong", content_type="text/plain")

def home_view(request):
    """A simple view for home'."""
    return HttpResponse("Welcome to HomePage. This Will be updated soon", content_type="text/plain")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop/", include("shop.urls")),
    path('ping/', ping_view, name='ping'), # Add the ping endpoint
    path('', home_view, name='home'), # Add the home endpoint

]