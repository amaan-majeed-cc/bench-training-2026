# Exercise 2: Weather CLI
# Use the Open-Meteo API (free, no key needed) to fetch current weather for any city.
# To get coordinates from a city name, use the Open-Meteo geocoding API first.
# Print: city, temperature (C and F), wind speed, weather description.
# This requires chaining two API calls. Figure out how.
# API docs: https://open-meteo.com/en/docs

import requests
import sys

weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle: Light intensity",
    53: "Drizzle: Moderate intensity",
    55: "Drizzle: Dense intensity",
    56: "Freezing Drizzle: Light intensity",
    57: "Freezing Drizzle: Dense intensity",
    61: "Rain: Slight intensity",
    63: "Rain: Moderate intensity",
    65: "Rain: Heavy intensity",
    66: "Freezing Rain: Light intensity",
    67: "Freezing Rain: Heavy intensity",
    71: "Snow fall: Slight intensity",
    73: "Snow fall: Moderate intensity",
    75: "Snow fall: Heavy intensity",
    77: "Snow grains",
    80: "Rain showers: Slight",
    81: "Rain showers: Moderate",
    82: "Rain showers: Violent",
    85: "Snow showers: Slight",
    86: "Snow showers: Heavy",
    95: "Thunderstorm: Slight or moderate",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

def get_weather(city):
    geocoding_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json'
    geocoding_response = requests.get(geocoding_url)
    # print(f'-----------------------------------------\nGeocoding Response: {geocoding_response.json()} {geocoding_response}\n-----------------------------------------')
    if 'results' in geocoding_response.json():
        latitude = geocoding_response.json()['results'][0]['latitude']
        longitude = geocoding_response.json()['results'][0]['longitude']
        city_name = geocoding_response.json()['results'][0]['name']

        weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
        weather_response = requests.get(weather_url)
        # print(f'-----------------------------------------\nWeather Response: {weather_response.json()}\n-----------------------------------------')
        if weather_response.status_code == 200:
            print(f'City: {city_name}')
            if weather_response.json()["current_weather_units"]["temperature"] == "°C":
                print(f'Temperature: {weather_response.json()["current_weather"]["temperature"]}°C ({weather_response.json()["current_weather"]["temperature"] * 1.8 + 32}°F)')
            else:
                print(f'Temperature: {weather_response.json()["current_weather"]["temperature"]}°F ({weather_response.json()["current_weather"]["temperature"] - 32}°C)')

            print(f'Wind Speed: {weather_response.json()["current_weather"]["windspeed"]} {weather_response.json()["current_weather_units"]["windspeed"]}')
            print(f'Weather Description: {weather_codes[weather_response.json()["current_weather"]["weathercode"]]}')
        else:
            print(f'Error: Something went wrong while fetching weather data')
    else:
        print(f'Error: Please provide a valid city name')
if __name__ == '__main__':
    city = sys.argv[1]
    get_weather(city)