# Imports
import pandas as pd
import requests

from environment.variables import WEATHER_KEY, LOC_LAT, LOC_LON, REQUEST_TIMEOUT


def get_weather_data(lat: str = LOC_LAT, lon: str = LOC_LON)->list:
    
    url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={lat},{lon}&aqi=no"
    request = requests.get(url, timeout=REQUEST_TIMEOUT).json()
    data = pd.DataFrame(request)
    cloud_percentage = int(data[data.index == "cloud"]["current"].iloc[0])
    visibility_km = int(data[data.index == "vis_km"]["current"].iloc[0])
    rain_mm = float(data[data.index == "precip_mm"]["current"].iloc[0])
    weather_list = {"cloud": cloud_percentage, "visibility": visibility_km, "rain": rain_mm}
    
    return weather_list
    