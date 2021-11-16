from django.urls import path
from appMain import views

urlpatterns = [
    path('', views.weather_report, name='index')
]
