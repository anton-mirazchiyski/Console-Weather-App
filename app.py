import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv('WEATHER_API_KEY')


def validate_user_input(city_name):
    return city_name.isalpha()


def get_user_input(text='Enter city name: '):
    city_name = input(text)
    result = validate_user_input(city_name)
    return get_user_input(text='Enter a valid city name: ') if not result else city_name


def get_city_coordinates_from_city_name(city_name):
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    params_dict = {'q': city_name, 'appid': API_key,}

    response = requests.get(url, params=params_dict)
    data = response.json()
    latitude, longitude = None, None

    for element in data:
        for key, value in element.items():
            if key == 'lat':
                latitude = value
            if key == 'lon':
                longitude = value
                break

    return latitude, longitude


def get_current_weather_info_from_coordinates(latitude, longitude):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params_dict = {'lat': latitude, 'lon': longitude, 'appid': API_key, 'units': 'metric'}

    response = requests.get(url, params=params_dict)
    data = response.json()

    weather_info = {}

    for key, value in data.items():
        if key == 'weather':
            weather = value[0].get('main')
            weather_info['Weather'] = weather
            description = value[0].get('description')
            weather_info['Description'] = description.capitalize()
        if key == 'main':
            temperature = value.get('temp')
            weather_info['Temperature'] = f'{temperature} degrees Celsius'
            humidity = value.get('humidity')
            weather_info['Humidity'] = humidity
            break

    return weather_info


def print_weather_info_of_a_city(weather_info, city_name):
    print(f'\nCurrent weather of {city_name}:\n')

    for key, value in weather_info.items():
        if key != 'Weather':
            print(f'{key}: {value}')
        else:
            print(value)


def main():
    user_input = get_user_input()
    city_name = user_input.capitalize()
    latitude, longitude = get_city_coordinates_from_city_name(city_name)
    weather_info = get_current_weather_info_from_coordinates(latitude, longitude)
    print_weather_info_of_a_city(weather_info, city_name)


if __name__ == '__main__':
    main()
