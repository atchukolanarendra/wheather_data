import requests

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, cities):
    weather_data = {}
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    for city in cities:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Get temperature in Celsius
        }
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            weather_data[city] = response.json()
        else:
            print(f"Error fetching data for {city}: {response.status_code}")
    
    return weather_data
