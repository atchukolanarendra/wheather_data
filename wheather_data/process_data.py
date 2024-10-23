from datetime import datetime
from collections import defaultdict

# Process weather data and organize by date
def process_weather_data(weather_data, daily_summaries):
    for city, data in weather_data.items():
        temp = data['main']['temp']
        weather_condition = data['weather'][0]['main']
        timestamp = data['dt']
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        
        if city not in daily_summaries:
            daily_summaries[city] = defaultdict(list)

        daily_summaries[city][date].append({
            'temp': temp,
            'weather_condition': weather_condition
        })

# Calculate daily aggregates
def calculate_daily_aggregates(daily_summaries):
    aggregates = {}
    
    for city, days in daily_summaries.items():
        aggregates[city] = {}
        for date, records in days.items():
            temps = [r['temp'] for r in records]
            conditions = [r['weather_condition'] for r in records]
            
            avg_temp = sum(temps) / len(temps)
            max_temp = max(temps)
            min_temp = min(temps)
            dominant_condition = max(set(conditions), key=conditions.count)
            
            aggregates[city][date] = {
                'average_temp': avg_temp,
                'max_temp': max_temp,
                'min_temp': min_temp,
                'dominant_condition': dominant_condition
            }
    
    return aggregates
