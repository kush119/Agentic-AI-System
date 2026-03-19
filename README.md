# Agentic AI System

This project contains multiple components: backend (FastAPI), frontend (Angular), MCP server, and a Streamlit interface.

## Components

### Backend (FastAPI)

- Location: `backend/`
- Requirements: `backend/requirements.txt`
- Run: `uvicorn app.main:app --reload` from `backend/` directory

```
Frontend (Angular)
```

- Location: `frontend/`
- Requirements: `frontend/package.json`
- Run:
  ```

  ng server
  ```

  from frontend/ directory

### MCP Server

- Location: `mcp/`
- Requirements: `mcp/requirements.txt`

### Streamlit Interface

- File: `interface.py`
- Requirements: `requirements_interface.txt`
- Run: `streamlit run interface.py`

## Setup

1. Install backend dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Install frontend dependencies:

   ```bash
   cd frontend
   npm install
   ```
3. Install Streamlit interface dependencies:

   ```bash
   pip install -r requirements_interface.txt
   ```
4. Install MCP dependencies:

   ```bash
   cd mcp
   pip install -r requirements.txt
   ```

## Running the System

1. Start the backend:

   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
2. Start the Angular frontend:

   ```bash
   cd frontend
   npm start
   ```
3. Or run the Streamlit interface:

   ```bash
   streamlit run interface.py
   ```

The Streamlit interface provides a simple chat UI that communicates with the backend API.
