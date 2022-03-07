from django.urls import path
from . import views

app_name='weather'

urlpatterns = [
    path('weather',views.weather_view, name='weather-view'),
    path('delete/<int:id>',views.delete_view,name='delete-view')
]