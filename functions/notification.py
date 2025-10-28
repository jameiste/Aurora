# Notification
import pandas as pd
import numpy as np
import json
import requests

# Local imports
from environment.variables import NOTIFICATION_KEY, ALERT, DEVICE, LOC_LAT, LOC_LON
from functions.score_validation import score_validation
from functions.weather_conditions import get_weather_data

# Function: If data is received send it for notification
def aurora_alert():
    
    # Get information
    send_message, data = score_validation()
    
    if send_message:
        score = np.mean(data["score"])
        forecast_time = pd.to_datetime(data["Forecast Time"].iloc[0])
        time = forecast_time.strftime("%H:%M")
        possible_wording_title = {1: "likely", 2: "very likely", 3: "visible"}
        possible_wording_text = {1: "", 2: "likely", 3: "dramatically"}
        if score >= 10:
            key = 3
        elif score >= 3:
            key = 2
        else:
            key = 1
            
        # Analysis of the Weather
        weather = get_weather_data(LOC_LAT, LOC_LON)
        cloud_percentage = weather["cloud"]
        rain_mm = weather["rain"]
        visibility_km = weather["visibility"]
        cloud_message = ""
        if cloud_percentage > 30:
            cloud_message = f"However it is cloudy with {cloud_percentage}% clouded sky ☁️ with {rain_mm}mm and a visibility of {visibility_km}km."
        else:
            cloud_message = f"Yeah, the visibilty with {visibility_km}km is good an only {cloud_message}% is low 🌉"

        title = f"🌌 Aurora Lights are {possible_wording_title.get(key)} ✨"
        text = f"There is a {possible_wording_text.get(key)} chance of ({score:.2f}) at {time} of seeing Polar Lights \n" + cloud_message
        pushcut_notify(title=title, text=text)

# Function: Send the message
def pushcut_notify(title: str, text: str, device: str | None = None):
    url = f"https://api.pushcut.io/v1/notifications/{ALERT}"
    headers = {
        "API-Key": NOTIFICATION_KEY,
        "Content-Type": "application/json",
    }
    body = {"title": title, "text": text}
    if device:         
        body["devices"] = [device]
    r = requests.post(url, headers=headers, json=body, timeout=10)
    r.raise_for_status()
    return r.json()