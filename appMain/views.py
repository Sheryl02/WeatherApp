from django.shortcuts import render
import urllib.request
# The 'urllib.request' module defines functions and classes which help in opening URLs (mostly HTTP)
# in a complex world — basic and digest authentication, redirections, cookies and more.
import json

def weather_report(request):
    if request.method == 'POST':
        city = request.POST['city']

        report_source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=4bec02fdfd9f40551de9fa60cbfef8cf').read()
        # report_source contains JSON data from API

        # report_source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?q=' +city+ '&cnt={cnt}&appid=4bec02fdfd9f40551de9fa60cbfef8cf').read()

        list_of_data = json.loads(report_source) #json data converted into a dictionary

        # data for variable list_of_data
        data = {
            'city':city,
            'country_code':str(list_of_data['sys']['country']),
            'coordinate':str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            'temp':str(list_of_data['main']['temp']) + '°C',
            'pressure':str(list_of_data['main']['pressure']),
            'humidity':str(list_of_data['main']['humidity']),
            'description':str(list_of_data['weather'][0]['description']),
            'icon':str(list_of_data['weather'][0]['icon']),
        }

        # print(data)

    else:
        data={}

    return render(request, 'appMain/index.html', data)

# Create your views here.
