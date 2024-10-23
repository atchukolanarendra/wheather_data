from flask import Flask, render_template
from fetch_weather import fetch_weather_data
from process_data import process_weather_data, calculate_daily_aggregates
from database import store_aggregates_in_db, get_aggregates_from_db
import time
import threading

app = Flask(__name__)

# Configuration
API_KEY = 'b2aef07d5716a392c2c9315de3631b3c'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
UPDATE_INTERVAL = 300  # 5 minutes in seconds

# Fetch and process data at regular intervals
def run_weather_updates():
    while True:
        # Fetch weather data
        weather_data = fetch_weather_data(API_KEY, CITIES)
        daily_summaries = {}
        process_weather_data(weather_data, daily_summaries)
        aggregates = calculate_daily_aggregates(daily_summaries)
        store_aggregates_in_db(aggregates)
        time.sleep(UPDATE_INTERVAL)

# Start a background thread to fetch weather data
def start_background_thread():
    thread = threading.Thread(target=run_weather_updates)
    thread.daemon = True  # Daemonize the thread so it shuts down when the main app does
    thread.start()

# Route to display weather data
@app.route('/')
def index():
    weather_data = get_aggregates_from_db()
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    start_background_thread()  # Start fetching weather data in the background
    app.run(debug=True)
