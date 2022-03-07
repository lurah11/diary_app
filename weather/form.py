from .models import City 
from django.forms import ModelForm
from django.core.exceptions import ValidationError
import requests
from django.conf import settings

class CityForm(ModelForm):
    class Meta: 
        model = City 
        fields = ['name']
        labels = {
            'name': 'Masukkan nama kota'
        }
    # def clean_name(self):
    #     data = self.cleaned_data.get('name')
    #     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    #     r = requests.get(url.format(data,settings.WEATHER_API_KEY)).json()
    #     if not r['cod'] == 200 :
    #         raise ValidationError('Kota tidak dikenal')
    #     if City.objects.filter(name__icontains=data):
    #         raise ValidationError('Kota sudah ada di database, tambahlah kota yang lain')
    #     return data