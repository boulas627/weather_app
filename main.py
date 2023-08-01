# This app is meant to help users understand what the weather is in thier desired location

# site: https://weatherstack.com/dashboard
# Password: weatherapi
# api key = 5bcaf59d48b073f029ed2145a79fdb29
# documentation: https://weatherstack.com/documentation

import requests 
import json

def read_api(params): 
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()  
    return api_response  

# print('Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))

def celsius_to_far(cels_temp): 
    far_temp = (cels_temp * (9/5) + 32)
    return int(far_temp)

def get_temp(api_response): 
    temp = api_response["current"]["temperature"]
    far_temp = celsius_to_far(temp)
    return far_temp

def get_wind_speed(api_response): 
    wind_speed = api_response["current"]["wind_speed"]
    return wind_speed

def get_weather_description(api_response): 
    description = api_response["current"]["weather_descriptions"]

def get_local_time(api_response): 
    time = api_response["location"]["localtime"]
    return time

city = input("What city would you like to get data for? ")

params = {
    "access_key": "5bcaf59d48b073f029ed2145a79fdb29",
    "query": str(city),
    "unit": "f"
}

weather_data = read_api(params)

final_temp = get_temp(weather_data)
print("The temperature in fahrenheit for {} is {} degrees fahrenheit".format(city, final_temp))

final_weather_description = get_weather_description(weather_data)
print("The weather in {} is {}".format(city, final_weather_description))

local_time = get_local_time(weather_data)
print("The local date and time in {} is {}".format(city, local_time))



{'request': {'type': 'City', 'query': 'London, United Kingdom', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'London', 'country': 'United Kingdom', 'region': 'City of London, Greater London', 'lat': '51.517', 'lon': '-0.106', 'timezone_id': 'Europe/London', 'localtime': '2023-07-31 02:18', 'localtime_epoch': 1690769880, 'utc_offset': '1.0'}, 'current': {'observation_time': '01:18 AM', 'temperature': 17, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast'], 'wind_speed': 20, 'wind_degree': 220, 'wind_dir': 'SW', 'pressure': 1008, 'precip': 0, 'humidity': 88, 'cloudcover': 100, 'feelslike': 17, 'uv_index': 1, 'visibility': 10, 'is_day': 'no'}}


# keep terminal open to run daily? Also can use cron job 