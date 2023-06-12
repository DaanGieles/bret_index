
import requests
import json
from datetime import datetime,timedelta
from pytz import timezone
def load_forecast():

    cet = timezone('Europe/Amsterdam')
    utc = timezone('UTC')

    date = datetime.now()
    datetime_formatted = date.strftime('%Y-%m-%d')+'T17:00'
    print(datetime_formatted)
    bret_json = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.39&longitude=4.84&current_weather=true&timezone=Europe/Berlin&hourly=temperature_2m,windspeed_10m').json()
    temp_hourly = dict(zip(bret_json['hourly']['time'],bret_json['hourly']['temperature_2m']))
    print(temp_hourly)
    forecast_temp = temp_hourly[datetime_formatted]
    return forecast_temp


def determine_bret_index(temp):
    
    bret_index = (temp-18)/5
    if bret_index>3:
        bret_index=3
    if bret_index<0:
        bret_index=0
    return round(bret_index,2)

if __name__ == '__main__':
    test = load_forecast()
    print(test)
