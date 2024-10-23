import sqlite3

# Store aggregates in the database
def store_aggregates_in_db(aggregates):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
        city TEXT,
        date TEXT,
        avg_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_condition TEXT
    )''')

    for city, days in aggregates.items():
        for date, summary in days.items():
            cursor.execute('''INSERT INTO daily_summary
                              (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (city, date, summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))

    conn.commit()
    conn.close()

# Retrieve weather data from the database
def get_aggregates_from_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM daily_summary")
    rows = cursor.fetchall()
    
    data = {}
    for row in rows:
        city, date, avg_temp, max_temp, min_temp, dominant_condition = row
        if city not in data:
            data[city] = []
        data[city].append({
            'date': date,
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        })
    
    conn.close()
    return data
