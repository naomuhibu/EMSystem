from django.urls import path
from .views import EarthquakeAPI

urlpatterns = [
    path('Earthquake/api', EarthquakeAPI.as_view(), name='Earthquake_API'),
]