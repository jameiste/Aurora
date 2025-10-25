# Ask for the data
import requests
import pandas as pd
import numpy as np

# Local Imports

from environment.variables import LOC_LAT, LOC_LON, REQUEST_TIMEOUT

# Function: Request the data 
def get_data():
    url = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"
    request = requests.get(url, timeout=REQUEST_TIMEOUT).json()
    data = pd.DataFrame(request)
    date_columns = ["Observation Time", "Forecast Time"]
    data[date_columns] = data[date_columns].apply(pd.to_datetime, errors="coerce", utc=True)
    # Go for closes coordinates
    data[["lon", "lat", "score"]] = pd.DataFrame(data["coordinates"].tolist(), index=data.index)
    data = data.drop(columns=["coordinates"])
    data["coordinates"] = data.apply(lambda row: [row["lon"], row["lat"]], axis=1)
    lon, lat, idw_score, index_range = get_locations_in_range(data, LOC_LON, LOC_LAT, radius_km=50) # 1 degree grid
    
    # Get data
    data_radius = data.iloc[index_range]
    
    return data_radius, data
    
    

# Function, get important radius data
def get_locations_in_range(df, ref_lon, ref_lat, lon_col="lon", lat_col="lat", score_col="score", radius_km: int =20)->list[float, float, float, int]:
    
    # Computations on Lat, Lon
    RAD = np.pi / 180.0
    lon1, lat1 = df[lon_col].to_numpy() * RAD, df[lat_col].to_numpy() * RAD
    lon2, lat2 = float(ref_lon) * RAD, float(ref_lat) * RAD
    dlon, dlat = lon1 - lon2, lat1 - lat2
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    d_km = 2 * 6371.0088 * np.arcsin(np.sqrt(a))

    # Find all points within radius
    in_range_idx = np.flatnonzero(d_km <= radius_km)

    if len(in_range_idx) == 0:
        # No points in radius → fallback to nearest
        nearest_idx = int(np.argmin(d_km))
        nearest = df.iloc[nearest_idx]
        idw4_score = float(nearest[score_col])
    else:
        # Compute IDW-4 with up to 4 nearest points within radius
        k = min(4, len(in_range_idx))
        local_dists = d_km[in_range_idx]
        neigh_idx = in_range_idx[np.argpartition(local_dists, k - 1)[:k]]
        w = 1 / np.clip(d_km[neigh_idx], 1e-6, None)
        w /= w.sum()
        idw4_score = float((df.iloc[neigh_idx][score_col].to_numpy() * w).sum())
        nearest = df.iloc[in_range_idx[np.argmin(local_dists)]]

    return nearest[lon_col], nearest[lat_col], idw4_score, in_range_idx