import requests 
import pandas as pd

# API URL
url = "https://www4.icao.int/doc8643/External/AircraftTypes"

# Req header
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Referer": "https://www4.icao.int/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}


# API call
response = {}
response = requests.post(url, headers=headers, json=response)

try:
    response.raise_for_status()
    data = response.json() 
    df = pd.DataFrame(data)
    df.to_csv("icao_aircraft_types.csv", index=False)
    print(f"API status code is {response.status_code}! All data is save in 'icao_aircraft_types.csv'")
except requests.exceptions.HTTPError as e:
    print(f"Something went worng: {e}")   
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")