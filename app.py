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
            weather_info[key] = value
        if key == 'main':
            weather_info[key] = value
            break

    return weather_info


def main():
    user_input = get_user_input()
    city_name = user_input.upper()
    latitude, longitude = get_city_coordinates_from_city_name(city_name)
    weather_info = get_current_weather_info_from_coordinates(latitude, longitude)


if __name__ == '__main__':
    main()
