from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool(tags={"sats", "flight"})
async def get_flight_status(flight_number: str) -> dict:
    """
    Get flight status for a given flight number.
    (Mock implementation – SATS API will be plugged later)
    """
    return {
        "flight_number": flight_number,
        "status": "ON_TIME",
        "departure": "SIN",
        "arrival": "DEL",
        "departure_time": "2026-03-15T10:00:00",
        "arrival_time": "2026-03-15T15:30:00"
    }


@mcp.tool(tags={"sats", "cargo"})
async def get_cargo_status(cargo_id: str) -> dict:
    """
    Get cargo status by cargo ID.
    (Mock implementation)
    """
    return {
        "cargo_id": cargo_id,
        "status": "IN_TRANSIT",
        "current_location": "SINGAPORE",
        "expected_delivery": "2026-03-16"
    }