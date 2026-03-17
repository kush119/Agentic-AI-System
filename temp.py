import certifi_win32
import requests

url = "https://opensky-network.org/api/states/all"

params = {
    "lamin": 12.0,
    "lomin": 77.0,
    "lamax": 13.5,
    "lomax": 78.5
}

r = requests.get(url, params=params, timeout=30)

print(r.status_code)
print(r.text[:500])