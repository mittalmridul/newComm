from django.urls import path

from . import views

urlpatterns = [
    path("ping/", views.home_view, name="shop_ping"),
]