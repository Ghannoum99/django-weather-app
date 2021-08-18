from http.client import InvalidURL
from urllib.error import HTTPError

from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import json


# Create your views here.

def index(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city +
                                            '&units=metric&appid=3633dbbb6ca4a65ce8193695165d0cab').read()
            list_of_data = json.loads(source)
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ',' +str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) ,
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": list_of_data['weather'][0]['icon'],
            }
        else:
            data = {}
        return render(request, 'weather_app/weather.html', data)
    except HTTPError:
        return HttpResponse('<h1>an error has occurred</h1>')
    except InvalidURL:
        return HttpResponse('<h1>an error has occurred</h1>')
    except UnicodeEncodeError:
        return HttpResponse('<h1>an error has occurred</h1>')

