from django.shortcuts import render, redirect
from .models import City
from .form import CityForm
import requests
from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import JsonResponse

# Create your views here.
def weather_view(request):
    weather_data = []
    no_city = ""
    err_msg = request.session.get('err_msg','')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            r = requests.get(url.format(new_city,settings.WEATHER_API_KEY)).json()
            if r['cod'] == 200:
                if City.objects.filter(name__icontains=new_city):
                    request.session['err_msg'] = f"{new_city}:Nama kota sudah ada di database"
                    # err_msg="Nama kota sudah ada di database"
                else : 
                    city = City(name=new_city)
                    city.save()
            else : 
                    request.session['err_msg'] = f"{new_city}:Nama kota tidak dikenal"
        return redirect('weather:weather-view')
    else : 
        if City.objects.all():
            cities = City.objects.all() 
            for city in cities:
                r = requests.get(url.format(city.name,settings.WEATHER_API_KEY)).json()
                city_weather  = {
                    'id' : city.id,
                    'name' : city.name,
                    'temp' : r['main']['temp'],
                    'desc' : r['weather'][0]['description'],
                    'icon' : r['weather'][0]['icon']
                }
                weather_data.append(city_weather)
        else : 
            no_city = "Anda Belum menambahkan kota"
    
    form = CityForm()
    context = {
        'form':form,
        'no_city':no_city,
        'weather_data':weather_data,
        'err_msg':err_msg 
    }
    request.session['err_msg']=""
    return render (request,'weather/weather.html',context=context)

def delete_view(request,id):
    if request.method=='POST':
        city = City.objects.get(id=id)
        city.delete()
    return redirect('weather:weather-view')




            
            