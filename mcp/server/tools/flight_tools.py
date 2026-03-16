import requests

BASE_URL = "https://opensky-network.org/api"


async def get_aircraft_track(icao24: str, t: int = 0) -> dict:
    """
    Get full flight trajectory (waypoints) for a specific aircraft.

    Args:
        icao24: ICAO24 hex address of aircraft (lowercase, e.g. 'abc123')
        t: Unix timestamp (0 = live/most recent)

    Returns:
        Dictionary with callsign, start/end time, and list of waypoints.
    """
    params = {"icao24": icao24, "time": t}

    response = requests.get(f"{BASE_URL}/tracks/all", params=params)
    response.raise_for_status()

    data = response.json()
    if not data:
        return {"error": f"No track data found for aircraft {icao24}"}

    return data


async def get_flights_by_aircraft(
    icao24: str,
    begin: int,
    end: int
) -> dict:
    """
    Get all flights for a specific aircraft in a time range.
    Maximum time interval: 30 days.

    Args:
        icao24: ICAO24 hex address (lowercase, e.g. 'abc123')
        begin:  Start time as Unix timestamp (seconds since epoch)
        end:    End time as Unix timestamp (seconds since epoch)

    Returns:
        Dictionary with list of flights for that aircraft.
    """
    if end - begin > 2592000:  # 30 days
        return {"error": "Time interval exceeds maximum of 30 days."}

    params = {"icao24": icao24, "begin": begin, "end": end}

    response = requests.get(f"{BASE_URL}/flights/aircraft", params=params)
    response.raise_for_status()

    flights = response.json() or []

    return {
        "icao24": icao24,
        "total": len(flights),
        "flights": flights
    }


async def get_flights_from_interval(begin: int, end: int) -> dict:
    """
    Get all global flights within a time window.
    Maximum time interval: 2 hours.

    Args:
        begin: Start time as Unix timestamp
        end:   End time as Unix timestamp

    Returns:
        Dictionary with list of all flights in the interval.
    """
    if end - begin > 7200:  # 2 hours
        return {"error": "Time interval exceeds maximum of 2 hours."}

    params = {"begin": begin, "end": end}

    response = requests.get(f"{BASE_URL}/flights/all", params=params)
    response.raise_for_status()

    flights = response.json() or []

    return {
        "total": len(flights),
        "flights": flights
    }


async def get_airport_arrivals(
    airport: str,
    begin: int,
    end: int
) -> dict:
    """
    Get all arriving flights at a specific airport.
    Maximum time interval: 7 days.

    Args:
        airport: ICAO airport code (e.g. 'WSSS' for Singapore Changi)
        begin:   Start time as Unix timestamp
        end:     End time as Unix timestamp

    Returns:
        Dictionary with list of arriving flights.
    """
    if end - begin > 604800:  # 7 days
        return {"error": "Time interval exceeds maximum of 7 days."}

    params = {"airport": airport.upper(), "begin": begin, "end": end}

    response = requests.get(f"{BASE_URL}/flights/arrival", params=params)
    response.raise_for_status()

    flights = response.json() or []

    return {
        "airport": airport.upper(),
        "total": len(flights),
        "arrivals": flights
    }


async def get_airport_departures(
    airport: str,
    begin: int,
    end: int
) -> dict:
    """
    Get all departing flights from a specific airport.
    Maximum time interval: 7 days.

    Args:
        airport: ICAO airport code (e.g. 'WSSS' for Singapore Changi)
        begin:   Start time as Unix timestamp
        end:     End time as Unix timestamp

    Returns:
        Dictionary with list of departing flights.
    """
    if end - begin > 604800:  # 7 days
        return {"error": "Time interval exceeds maximum of 7 days."}

    params = {"airport": airport.upper(), "begin": begin, "end": end}

    response = requests.get(f"{BASE_URL}/flights/departure", params=params)
    response.raise_for_status()

    flights = response.json() or []

    return {
        "airport": airport.upper(),
        "total": len(flights),
        "departures": flights
    }