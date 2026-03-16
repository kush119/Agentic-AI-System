import logging
from fastmcp import FastMCP
from core.config import SERVER_NAME, SERVER_PORT

# Import tool functions
from tools.state_tools import get_live_states, get_states_by_area
from tools.flight_tools import (
    get_aircraft_track,
    get_flights_by_aircraft,
    get_flights_from_interval,
    get_airport_arrivals,
    get_airport_departures,
)

logging.basicConfig(level=logging.INFO)

# ─────────────────────────────────────────────
# FastMCP Server
# ─────────────────────────────────────────────
mcp = FastMCP(
    name=SERVER_NAME,
    instructions="""
    You are an aviation data tool server powered by the OpenSky Network.
    You provide real-time and historical flight data tools.
    Use the appropriate tool based on the user's query.
    """
)

# ─────────────────────────────────────────────
# Register State Tools
# ─────────────────────────────────────────────
mcp.tool(tags={"opensky", "states"})(get_live_states)
mcp.tool(tags={"opensky", "states"})(get_states_by_area)

# ─────────────────────────────────────────────
# Register Flight Tools
# ─────────────────────────────────────────────
mcp.tool(tags={"opensky", "flight"})(get_aircraft_track)
mcp.tool(tags={"opensky", "flight"})(get_flights_by_aircraft)
mcp.tool(tags={"opensky", "flight"})(get_flights_from_interval)
mcp.tool(tags={"opensky", "airport"})(get_airport_arrivals)
mcp.tool(tags={"opensky", "airport"})(get_airport_departures)


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=SERVER_PORT
    )