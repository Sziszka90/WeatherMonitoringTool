import requests
import utilities as util
from decouple import config

def queryFromAPI():
    data = {}
    dataToPlot = {}

    city = config('CITY')
    apiKey = config('API_KEY')
    urlSite = config('URL')

    url = urlSite + city + "&units=metric&appid=" + apiKey

    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)

    print(response)

    data['CelsiusTemp'] = response.json()['main']['temp']

    url = urlSite + city + "&units=imperial&appid=" + apiKey
    
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)

    data['FahrenheitTemp'] = response.json()['main']['temp']
    data['Sun']            = util.sunsetOrSunrise([response.json()['sys']['sunrise'],response.json()['sys']['sunset']])
    data['Mood']           = util.prediction(response.json()['clouds']['all'], data['CelsiusTemp'])
    data['City']           = city

    cities = config("CITIES").split(",")

    for city in cities:
        url = urlSite + city + "&units=metric&appid=" + apiKey
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)
        
        dataToPlot[city] = response.json()['main']['temp']

        
    
    return data, dataToPlot
