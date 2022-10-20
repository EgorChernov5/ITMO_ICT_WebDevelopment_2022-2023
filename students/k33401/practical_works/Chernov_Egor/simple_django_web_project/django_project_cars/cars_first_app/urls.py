from django.urls import path
from . import views


urlpatterns = [
    path('driver/', views.get_driver),
    path('drivers/', views.get_drivers),
]
