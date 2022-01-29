from typing import Dict
import requests
import utilities as util
from decouple import config

def query_from_api() -> Dict:
    data = {}
    data_to_plot = {}

    city = config('CITY')
    api_key = config('API_KEY')
    url_site = config('URL')

    url = url_site + city + "&units=metric&appid=" + api_key

    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)

    data['CelsiusTemp'] = response.json()['main']['temp']

    url = url_site + city + "&units=imperial&appid=" + api_key
    
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)

    data['FahrenheitTemp'] = response.json()['main']['temp']
    data['Sun']            = util.sunset_or_sunrise([response.json()['sys']['sunrise'],response.json()['sys']['sunset']])
    data['Mood']           = util.prediction(response.json()['clouds']['all'], data['CelsiusTemp'])
    data['City']           = city

    cities = config("CITIES").split(",")

    for city in cities:
        url = url_site + city + "&units=metric&appid=" + api_key
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)
        
        data_to_plot[city] = response.json()['main']['temp']
        data_to_plot["Budapest"] = 45.00
        data_to_plot["Warsaw"] = 15.00
        data_to_plot["Prague"] = 45.00
        data_to_plot["Wien"] = 25.00


    
    return data, data_to_plot
