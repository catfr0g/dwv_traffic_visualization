# Traffic Visualization System

This repository contains a system for visualizing real-time traffic data on a 3D globe. The system is composed of three main components:

1. **Sender**: Reads traffic data from a CSV file and sends it to the server.
2. **Server**: Processes incoming traffic data and serves it to the frontend.
3. **Frontend**: Displays the traffic data on a 3D globe using Three.js.


### Components

- **Sender**: 
  - Reads `ip_addresses.csv` and sends traffic data to the server at regular intervals.
  - Code: [sender/sender.py](sender/sender.py)
  - Dependencies: [sender/requirements.txt](sender/requirements.txt)

- **Server**:
  - A Flask-based server that receives traffic data from the sender and provides it to the frontend.
  - Code: [server/app.py](server/app.py)
  - Dependencies: [server/requirements.txt](server/requirements.txt)

- **Frontend**:
  - A web-based visualization using Three.js to display traffic data on a 3D globe.
  - Code: [frontend/index.html](frontend/index.html)

## Prerequisites

- Docker
- Docker Compose

## Setup and Usage

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Build and run the system:
    ```bash
   docker-compose up --build
   ```

3. Sender:
    - The sender reads data from ip_addresses.csv and sends it to the server.
    - The delay between sending data is based on the timestamps in the CSV file.

4. Server:
    - The server runs on http://localhost:5000.
    - Endpoint /data provides traffic data to the frontend.
5. Frontend:
    - Displays the traffic data on a 3D globe.
    - Recent IP addresses are shown in a sidebar.
    - Access the frontend: Open your browser and navigate to http://localhost.