import os
from dotenv import load_dotenv

load_dotenv()

SERVER_NAME = os.getenv("MCP_SERVER_NAME", "SATS-MCP-Server")
SERVER_PORT = int(os.getenv("MCP_SERVER_PORT", 9000))