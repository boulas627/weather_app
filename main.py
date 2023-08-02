# This app is meant to help users understand what the weather is in thier desired location

# site: https://weatherstack.com/dashboard
# documentation: https://weatherstack.com/documentation

import requests 
import json
import os 

api_key = os.environ["api_key"]

def read_api(params): 
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()  
    return api_response  

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
    "access_key": api_key,
    "query": str(city)
}

weather_data = read_api(params)

final_temp = get_temp(weather_data)
print("The temperature in fahrenheit for {} is {} degrees fahrenheit".format(city, final_temp))

final_weather_description = get_weather_description(weather_data)
print("The weather in {} is {}".format(city, final_weather_description))

local_time = get_local_time(weather_data)
print("The local date and time in {} is {}".format(city, local_time))


# keep terminal open to run daily? Also can use cron job 

# video to help write GitHub Actions and use Secrets as Env Variable 