# To Open the Project Files You need to click the Weather_data than you can see the project files
# Real-Time Data Processing System for Weather Monitoring
### Objective

The Real-Time Data Processing System continuously monitors weather data from the OpenWeatherMap API and provides summarized insights, including daily rollups and aggregates (such as average, max, min temperatures, and dominant weather conditions). The system also includes an alerting mechanism that triggers alerts when user-defined thresholds are breached.

# Features
Real-time weather data retrieval from OpenWeatherMap API for multiple Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
Data rollup and aggregate calculations:
  1.Average Temperature
  2.Maximum Temperature
  3.Minimum Temperature
  4.Dominant Weather Condition
Temperature conversion from Kelvin to Celsius/Fahrenheit based on user preference.
User-configurable alerting system based on temperature and weather condition thresholds.
Visualization for daily weather summaries and alerts.

# Table of Contents
Installation and Setup
Configuration
Architecture
Endpoints
Visualization
Sample Data
Testing
Artifacts
Screenshots
#  Installation and Setup
### Prerequisites

1.Python 3.8+

2.Flask (for web server)

3.SQLite (for database storage)

4.OpenWeatherMap API Key (get it here)
### Clone the Repository

git clone https://github.com/atchukolanarendra/wheather_data.git
cd weather-monitoring-system

### Setting up a Virtual Environment
It’s a good practice to set up a virtual environment:


python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

### Install Required Dependencies

pip install -r requirements.txt
### Environment Variables

Create a .env file in the root directory with your API key:

OPENWEATHERMAP_API_KEY="b2aef07d5716a392c2c9315de3631b3c"

### Database Setup

The application uses SQLite for storing weather summaries and alert logs. To create the database:

flask db init
flask db migrate
flask db upgrade

### Running the Application
 Start the Flask server:
   #### app.py

# Configuration

The system is configurable using environment variables:

  OPENWEATHERMAP_API_KEY: Your OpenWeatherMap API key.

CITIES: A list of Indian metros to track (e.g., "Delhi,Mumbai,Chennai").

UPDATE_INTERVAL: How frequently to fetch data from the OpenWeatherMap API (default: every 5 minutes).

TEMP_UNIT: Unit for temperature conversion (Celsius or Fahrenheit).

These can be updated in the .env file.

# Architecture

This system is designed in a three-tier architecture:

###### Frontend (UI):Displays weather summaries, historical data, and alerts.
###### Backend (API): Responsible for fetching real-time weather data, performing rollups/aggregates, and handling alerts.
###### Data Layer (Database): SQLite is used to store daily weather summaries and alerts.

# Endpoints

### GET /weather-summary
Returns the daily weather summary for each metro city.

### POST /set-threshold
Set thresholds for alerts based on temperature or weather conditions.

### GET /alerts
Fetch all triggered alerts.

#  Visualization
Real-time data visualization using Chart.js or any JavaScript charting library.
Graphs for:
Temperature trends (average, max, min).
Alerts over time.

Sample visualizations can be displayed on the /dashboard endpoint.

## Sample Data

| City     | Temperature (°C) | Feels Like (°C) | Weather Condition | Timestamp           |
|----------|------------------|-----------------|-------------------|---------------------|
| Delhi    | 34.5              | 35.1            | Clear             | 2024-10-22 12:00:00 |
| Mumbai   | 29.8              | 30.5            | Rain              | 2024-10-22 12:05:00 |
| Chennai  | 32.1              | 33.0            | Clear             | 2024-10-22 12:10:00 |

# Testing
## Test Cases
#### System Setup:
Test that the system connects to the OpenWeatherMap API using a valid API key.

#### Data Retrieval:
Simulate weather API calls and ensure the system correctly retrieves and processes data.

#### Temperature Conversion:
Test conversion from Kelvin to Celsius or Fahrenheit, based on user preferences.

#### Daily Weather Summary:
Simulate several days of weather data and verify that average, max, min, and dominant conditions are calculated accurately.

#### Alerting System:
Test with sample weather data that exceeds the configured threshold and verify that alerts are triggered.


# The Output interface for weather data is:
![image11](https://github.com/user-attachments/assets/a879ce32-1565-46d3-b177-78a15e03fbbe)
![image22](https://github.com/user-attachments/assets/1fb8dca5-441b-4ac6-bfed-54ff95ce2b09)
![image33](https://github.com/user-attachments/assets/517f530d-01c6-4423-a051-a72e1d049ce5)
![image44](https://github.com/user-attachments/assets/2d2af906-4b95-4657-b6c7-68253df85f7f)
![image55](https://github.com/user-attachments/assets/0c63ef45-516a-4e0c-918d-83d427f0c6d6)
![image66](https://github.com/user-attachments/assets/82bcc332-b6cf-45bb-8ee1-f32b1e9c5cc1)


