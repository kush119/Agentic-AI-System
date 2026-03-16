import requests
from typing import Optional

BASE_URL = "https://opensky-network.org/api"


async def get_live_states(icao24: list[str] = None) -> dict:
    """
    Get live position and status of all aircraft currently in the airspace.
    Optionally filter by a list of ICAO24 addresses.

    Args:
        icao24: Optional list of ICAO24 hex addresses (e.g. ['abc123'])

    Returns:
        Dictionary with list of live aircraft state vectors.
    """
    params = {}
    if icao24:
        # OpenSky accepts multiple icao24 as repeated query params
        params["icao24"] = icao24

    response = requests.get(f"{BASE_URL}/states/all", params=params)
    response.raise_for_status()

    data = response.json()
    states = data.get("states") or []

    return {
        "total": len(states),
        "states": states
    }


async def get_states_by_area(
    min_lat: float,
    max_lat: float,
    min_lon: float,
    max_lon: float
) -> dict:
    """
    Get live aircraft states within a geographic bounding box.

    Args:
        min_lat: Minimum latitude  (e.g. 1.0 for Singapore area)
        max_lat: Maximum latitude  (e.g. 2.0)
        min_lon: Minimum longitude (e.g. 103.0)
        max_lon: Maximum longitude (e.g. 104.5)

    Returns:
        Dictionary with list of aircraft within the bounding box.
    """
    params = {
        "lamin": min_lat,
        "lamax": max_lat,
        "lomin": min_lon,
        "lomax": max_lon
    }

    response = requests.get(f"{BASE_URL}/states/all", params=params)
    response.raise_for_status()

    data = response.json()
    states = data.get("states") or []

    return {
        "total": len(states),
        "bbox": {
            "min_lat": min_lat,
            "max_lat": max_lat,
            "min_lon": min_lon,
            "max_lon": max_lon
        },
        "states": states
    }