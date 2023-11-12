from django.urls import path
from .views import EarthquakeAPI, IndexView

urlpatterns = [
    path('Earthquake/api', EarthquakeAPI.as_view(), name='Earthquake_API'),
    path('',IndexView .as_view(),name='index')
]