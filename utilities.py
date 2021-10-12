from datetime import datetime, timedelta

def sunset_or_sunrise(items: list) -> dict:

    result = {}

    time_now = datetime.now().timestamp()

    time_set_rise = min(items, key=lambda x: abs(x - time_now))

    if(time_set_rise == items[0]):
        if(time_set_rise > time_now):
            result['Sunrise'] = str(timedelta(seconds=(time_set_rise - time_now)))
            return result 
        else:
            result['Sunrise'] = '-' + str(timedelta(seconds=(time_now - time_set_rise)))
            return result  
    else:
        if(time_set_rise > time_now):
            result['Sunset'] = str(timedelta(seconds=(time_set_rise - time_now)))
            return result 
        else:
            result['Sunset'] = '-' + str(timedelta(seconds=(time_now - time_set_rise)))
            return result  


def prediction(cloudiness: int, temp: float) -> str:
    cloudiness = abs(cloudiness - 100)

    if cloudiness == 0:
        cloudiness = 1
        
    if(0 < temp <= 25):
        happiness = int((temp/25) * cloudiness)
    elif(25 < temp <= 50):
        happiness =  int((25/temp) * cloudiness)
    else:
        happiness = 0

    if(happiness < 25):
        return "Depressed"
    elif( 25 <= happiness < 50):
        return "Miserable"
    elif( 50 <= happiness < 75):
        return "Optimistic"
    else:
        return "Happy"



