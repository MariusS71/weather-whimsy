import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(lat: float = 44.43225, lon: float = 26.10626):
    """Fetch weather data for given coordinates (default = Bucharest)."""
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Pick only what we need
        return {
            "city": data.get("name", "Unknown"),
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "main": data["weather"][0]["main"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    except requests.RequestException as e:
        print("Error fetching weather:", e)
        return None
