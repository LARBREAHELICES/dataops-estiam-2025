import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta
from typing import List, Union, cast

# Number of rows to generate
n_rows: int = 200

# Possible device IDs
device_ids: List[str] = ['abc123', 'abcXYZ', 'dev001', 'sensorA', 'iot999']

# Starting timestamp
base_time: datetime = datetime(2025, 5, 1, 12, 0)


def generate_cleaner_row(i: int) -> List[Union[str, float]]:
    """Generate a single row of cleaner IoT data."""
    timestamp: str = (base_time + timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S")
    device_id: str = random.choice(device_ids)

    # np.nan is a float, so Union[float, int] simplifies to float
    temp: float  = round(random.uniform(15, 35), 1) if random.random() > 0.05 else cast(float, "np.nan")
    hum: float = random.randint(30, 70) if random.random() > 0.05 else cast(float, "np.nan")
    noise_db: float = random.randint(50, 90) if random.random() > 0.1 else cast(float, "np.nan")
    pm25: float = random.randint(5, 30) if random.random() > 0.1 else cast(float, "np.nan")

    # Random location: Paris or NYC with jitter
    loc_choice: str = random.choice(["paris", "nyc"])
    if loc_choice == "paris":
        lat: float = 48.8566 + random.uniform(-0.01, 0.01)
        lon: float = 2.3522 + random.uniform(-0.01, 0.01)
    else:
        lat = 40.7128 + random.uniform(-0.01, 0.01)
        lon = -74.0060 + random.uniform(-0.01, 0.01)

    location: str = f"({lat:.5f},{lon:.5f})"

    return [timestamp, device_id, temp, hum, noise_db, pm25, location]


# Generate dataset
data_clean: List[List[Union[str, float]]] = [generate_cleaner_row(i) for i in range(n_rows)]

# Create DataFrame
df_clean: pd.DataFrame = pd.DataFrame(
    data_clean,
    columns=["timestamp", "device_id", "temp", "hum", "noise_db", "pm25", "location"]
)

# Export to CSV
df_clean.to_csv("iot_clean_data_200.csv", index=False)
print("Fichier iot_clean_data_200.csv généré avec succès !")
