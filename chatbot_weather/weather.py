import requests
import boto3

# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    ssm = boto3.client('ssm', region_name='us-east-1')
    parameter = ssm.get_parameter(Name='/openweathermap/api_key', WithDecryption=True)
    api_key = parameter['Parameter']['Value']
    #base_url = 'https://api.openweathermap.org/data/2.5/weather'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        return {'error': 'Unable to fetch weather data.'}


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)

# User interaction loop
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break

    if 'weather in' in user_input:
        city = user_input.replace('weather in', '').strip()
        weather_data = get_weather(city)
        if 'error' in weather_data:
            print('WeatherBot:', weather_data['error'])
        else:
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            temperature_celsius = fahrenheit_to_celsius(temperature)
            print(f'WeatherBot: The weather in {city} is {description} with a temperature of {temperature_celsius}°C.')

    else:
        print('WeatherBot: Sorry, I can only provide weather information. Ask something like "Weather in London" or "Exit" to end the conversation.')
