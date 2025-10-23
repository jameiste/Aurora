# Aurora Alert

**Aurora Alert** is checking the aurora forecast for a determined location and sends out a notification if 
a high likelihood of polar lights are reached in that region


## Features

- Fetches live aurora data from [NOAA SWPC OVATION model](https://services.swpc.noaa.gov/json/ovation_aurora_latest.json)
- Calculates local aurora probability using geographic coordinates (lat, lon)
- Triggers **Pushcut** notifications on iPhone when activity is high
- Runs continuously in a **Docker container** (auto-refreshes every `TIME_THRESHOLD` seconds)
- Built with async scheduling for stable, low-resource execution



##  Setup

### 1. Clone the repository

### 2. Create .env file
```bash
API_KEY=your_pushcut_key
ALERT_NAME=Aurora
DEVICE=Your_iPhone_Name
```
### 3. All other parameters are in variables defined

### 4. Create envvironment or docker container

Either:
```bash
conda create -f environment.yml
```
and run with
```bash
python main.py
```
Or create the Docker setup and run with
```bash
docker compose up -d --build
```
