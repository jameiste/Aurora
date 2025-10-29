# Set up all variables
from dotenv import load_dotenv
import os

load_dotenv()
# --- Location ---
LOC_LAT = 59.3293
LOC_LON = 18.0686 

# --- Threshold ---
TIME_THRESHOLD = 3600
REQUEST_TIMEOUT = 25

# --- Notification
NOTIFICATION_KEY = os.getenv("NOTIFICATION_API_KEY", "Fallback")
BARK_KEY = os.getenv("BARK_API_KEY", "Fallback")
WEATHER_KEY = os.getenv("WEATHER_API_KEY", "Fallback")
ALERT = os.getenv("ALERT_NAME", "Fallback")
DEVICE = os.getenv("DEVICE", None)