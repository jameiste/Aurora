# Notification
import pandas as pd
import numpy as np
import json
import requests

# Local imports
from environment.variables import KEY, ALERT, DEVICE
from functions.score_validation import score_validation

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

        title = f"🌌 Aurora Lights are {possible_wording_title.get(key)} ✨"
        text = f"There is a {possible_wording_text.get(key)} chance of ({score:.2f}) at {time} of seeing Polar Lights"
        pushcut_notify(title=title, text=text)

# Function: Send the message
def pushcut_notify(title: str, text: str, device: str | None = None):
    url = f"https://api.pushcut.io/v1/notifications/{ALERT}"
    headers = {
        "API-Key": KEY,
        "Content-Type": "application/json",
    }
    body = {"title": title, "text": text}
    if device:         
        body["devices"] = [device]
    r = requests.post(url, headers=headers, json=body, timeout=10)
    r.raise_for_status()
    return r.json()