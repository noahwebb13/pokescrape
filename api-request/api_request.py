import requests

api_key = "f84101bacab7b0b87de8bf2dc257ccdf"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=Chicago"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try: 
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.\n")
        print(f"{response.json()}\n")
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}\n")
        raise
    return response.json()
    


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Chicago, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Chicago', 'country': 'United States of America', 'region': 'Illinois', 'lat': '41.850', 'lon': '-87.650', 'timezone_id': 'America/Chicago', 'localtime': '2026-05-27 10:34', 'localtime_epoch': 1779878040, 'utc_offset': '-5.0'}, 'current': {'observation_time': '03:34 PM', 'temperature': 25, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '05:21 AM', 'sunset': '08:15 PM', 'moonrise': '05:04 PM', 'moonset': '03:01 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 83}, 'air_quality': {'co': '188.85', 'no2': '13.15', 'o3': '116', 'so2': '5.75', 'pm2_5': '20.85', 'pm10': '21.75', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 4, 'wind_degree': 32, 'wind_dir': 'NNE', 'pressure': 1017, 'precip': 0, 'humidity': 59, 'cloudcover': 0, 'feelslike': 25, 'uv_index': 4, 'visibility': 16, 'is_day': 'yes'}}

