# Set up all variables
from dotenv import load_dotenv
import os

load_dotenv()
# --- Location ---
LOC_LAT = 59.3293
LOC_LON = 18.0686 

# --- Probability ---
PROBABILITY = 0.3
TIME_THRESHOLD = 7200

# --- Notification
KEY = os.getenv("API_KEY", "Fallback")
ALERT = os.getenv("ALERT_NAME", "Fallback")
DEVICE = os.getenv("DEVICE", None)