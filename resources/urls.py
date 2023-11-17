from django.urls import path
from .views import EarthquakeList,EarthquakeAPI,IndexView #EarthquakeDetail,,Register,Login

urlpatterns = [
    path('',IndexView .as_view(),name='index'),
    path('earthquakes/', EarthquakeList.as_view(), name='earthquake-list'),
    path('Earthquake/api', EarthquakeAPI.as_view(), name='Earthquake_API'),
    #path('earthquakes/<int:pk>/', EarthquakeDetail.as_view(), name='earthquake-detail'),
    #path('register/', Register, name='register'),
    #path('login/', Login, name='login'),
]