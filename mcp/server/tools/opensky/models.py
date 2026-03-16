def serialize_state_vector(sv) -> dict:
    """
    Serialize a raw state vector list from OpenSky REST API to a clean dict.

    OpenSky returns each state as a list of values in fixed index order:
    [icao24, callsign, origin_country, time_position, last_contact,
     longitude, latitude, baro_altitude, on_ground, velocity,
     true_track, vertical_rate, sensors, geo_altitude, squawk,
     spi, position_source, category]
    """
    if not sv or not isinstance(sv, list):
        return {}

    return {
        "icao24":          sv[0],
        "callsign":        sv[1].strip() if sv[1] else None,
        "origin_country":  sv[2],
        "time_position":   sv[3],
        "last_contact":    sv[4],
        "longitude":       sv[5],
        "latitude":        sv[6],
        "baro_altitude":   sv[7],
        "on_ground":       sv[8],
        "velocity":        sv[9],
        "true_track":      sv[10],
        "vertical_rate":   sv[11],
        "geo_altitude":    sv[13],  # index 12 = sensors (omitted)
        "squawk":          sv[14],
        "category":        sv[17] if len(sv) > 17 else None,
    }


def serialize_flight_data(fd) -> dict:
    """
    Serialize a raw flight data dict from OpenSky REST API to a clean dict.

    OpenSky returns each flight as a JSON object with camelCase keys.
    """
    if not fd or not isinstance(fd, dict):
        return {}

    callsign = fd.get("callsign")

    return {
        "icao24":                        fd.get("icao24"),
        "first_seen":                    fd.get("firstSeen"),
        "last_seen":                     fd.get("lastSeen"),
        "departure_airport":             fd.get("estDepartureAirport"),
        "arrival_airport":               fd.get("estArrivalAirport"),
        "callsign":                      callsign.strip() if callsign else None,
        "departure_airport_horiz_dist":  fd.get("estDepartureAirportHorizDistance"),
        "departure_airport_vert_dist":   fd.get("estDepartureAirportVertDistance"),
        "arrival_airport_horiz_dist":    fd.get("estArrivalAirportHorizDistance"),
        "arrival_airport_vert_dist":     fd.get("estArrivalAirportVertDistance"),
        "departure_airport_candidates":  fd.get("departureAirportCandidatesCount"),
        "arrival_airport_candidates":    fd.get("arrivalAirportCandidatesCount"),
    }


def serialize_waypoint(wp) -> dict:
    """
    Serialize a raw waypoint list from OpenSky track data to a clean dict.

    OpenSky returns each waypoint as a list:
    [time, latitude, longitude, baro_altitude, true_track, on_ground]
    """
    if not wp or not isinstance(wp, list):
        return {}

    return {
        "time":          wp[0],
        "latitude":      wp[1],
        "longitude":     wp[2],
        "baro_altitude": wp[3],
        "true_track":    wp[4],
        "on_ground":     wp[5],
    }


def serialize_track(track) -> dict:
    """
    Serialize a raw flight track dict from OpenSky REST API to a clean dict.

    OpenSky returns track as a JSON object with a 'path' list of waypoints.
    """
    if not track or not isinstance(track, dict):
        return {}

    callsign = track.get("callsign")

    return {
        "icao24":     track.get("icao24"),
        "start_time": track.get("startTime"),
        "end_time":   track.get("endTime"),
        "callsign":   callsign.strip() if callsign else None,
        "waypoints":  [serialize_waypoint(wp) for wp in track.get("path") or []],
    }