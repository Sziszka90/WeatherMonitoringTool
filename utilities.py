from datetime import datetime, timedelta

def sunsetOrSunrise(items):

    result = {}

    timeNow = datetime.now().timestamp()

    timeSetRise = min(items, key=lambda x: abs(x - timeNow))

    if(timeSetRise == items[0]):
        if(timeSetRise > timeNow):
            result['Sunrise'] = str(timedelta(seconds=(timeSetRise - timeNow)))
            return result 
        else:
            result['Sunrise'] = '-' + str(timedelta(seconds=(timeNow - timeSetRise)))
            return result  
    else:
        if(timeSetRise > timeNow):
            result['Sunset'] = str(timedelta(seconds=(timeSetRise - timeNow)))
            return result 
        else:
            result['Sunset'] = '-' + str(timedelta(seconds=(timeNow - timeSetRise)))
            return result  


def prediction(cloudiness, temp):
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



