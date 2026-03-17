import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://opensky-network.org/"


class OpenSkyClient:
    def __init__(self):
        username = os.getenv("OPENSKY_USERNAME")
        password = os.getenv("OPENSKY_PASSWORD")

        # Use auth tuple if credentials are provided, else anonymous
        self.auth = (username, password) if username and password else None

    def _get(self, endpoint: str, params: dict = None) -> any:
        """
        Internal helper to make authenticated GET requests to OpenSky API.

        Args:
            endpoint: API path (e.g. '/states/all')
            params:   Query parameters dict

        Returns:
            Parsed JSON response or None if no content.
        """
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url, params=params, auth=self.auth)

        if response.status_code == 404:
            return None  # No data found for given params

        response.raise_for_status()

        # OpenSky returns empty body on some endpoints when no data
        if not response.content:
            return None

        return response.json()

    def get_live_states(self, icao24=None, bbox=None) -> list:
        params = {}
        if icao24:
            params["icao24"] = icao24
        if bbox:
            # bbox = (min_lat, max_lat, min_lon, max_lon)
            params["lamin"] = bbox[0]
            params["lamax"] = bbox[1]
            params["lomin"] = bbox[2]
            params["lomax"] = bbox[3]

        data = self._get("/states/all", params=params)
        return data.get("states") or [] if data else []

    def get_states_by_bbox(
        self,
        min_lat: float,
        max_lat: float,
        min_lon: float,
        max_lon: float
    ) -> list:
        return self.get_live_states(
            bbox=(min_lat, max_lat, min_lon, max_lon)
        )

    def get_aircraft_track(self, icao24: str, t: int = 0) -> dict | None:
        params = {"icao24": icao24, "time": t}
        return self._get("/tracks/all", params=params)

    def get_flights_by_aircraft(
        self,
        icao24: str,
        begin: int,
        end: int
    ) -> list:
        params = {"icao24": icao24, "begin": begin, "end": end}
        data = self._get("/flights/aircraft", params=params)
        return data or []

    def get_flights_from_interval(self, begin: int, end: int) -> list:
        params = {"begin": begin, "end": end}
        data = self._get("/flights/all", params=params)
        return data or []

    def get_airport_arrivals(
        self,
        airport: str,
        begin: int,
        end: int
    ) -> list:
        params = {"airport": airport.upper(), "begin": begin, "end": end}
        data = self._get("/flights/arrival", params=params)
        return data or []

    def get_airport_departures(
        self,
        airport: str,
        begin: int,
        end: int
    ) -> list:
        params = {"airport": airport.upper(), "begin": begin, "end": end}
        data = self._get("/flights/departure", params=params)
        return data or []