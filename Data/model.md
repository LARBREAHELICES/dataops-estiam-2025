
| Nom du champ | Type SQL           | Description                          | Contraintes          |
| ------------ | ------------------ | ------------------------------------ | -------------------- |
| `id`         | `SERIAL`           | Identifiant unique                   | `PRIMARY KEY` (auto) |
| `timestamp`  | `TIMESTAMP`        | Date et heure de la mesure           | `NOT NULL`           |
| `device_id`  | `VARCHAR(50)`      | Identifiant du capteur               | `NOT NULL`           |
| `temp`       | `REAL`             | Température mesurée (°C)             | Peut être `NULL`     |
| `hum`        | `REAL`             | Humidité relative (%)                | Peut être `NULL`     |
| `noise_db`   | `REAL`             | Niveau sonore (décibels)             | Peut être `NULL`     |
| `pm25`       | `REAL`             | Particules fines PM2.5 (µg/m³)       | Peut être `NULL`     |
| `location`   | `TEXT`             | Coordonnées brutes (ex. `(lat,lon)`) | Optionnel            |
| `lat`        | `DOUBLE PRECISION` | Latitude extraite                    | Peut être `NULL`     |
| `lon`        | `DOUBLE PRECISION` | Longitude extraite                   | Peut être `NULL`     |
| `city`       | `VARCHAR(30)`      | Ville détectée (`Paris`, `New York`) | Peut être `NULL`     |
| `hour`       | `SMALLINT`         | Heure de la journée (0–23)           | Peut être `NULL`     |
| `day`        | `SMALLINT`         | Jour du mois (1–31)                  | Peut être `NULL`     |
