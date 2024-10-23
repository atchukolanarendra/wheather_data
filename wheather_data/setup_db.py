import sqlite3

def create_weather_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    # Drop the table if it already exists (use this only if you don't need the existing data)
    cursor.execute('''DROP TABLE IF EXISTS weather_data''')

    # Create the table with the 'timestamp' column
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temp REAL,
        feels_like REAL,
        condition TEXT,
        dt INTEGER,
        timestamp INTEGER
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Table 'weather_data' created with the correct schema.")

# Call the function to create the table
if __name__ == '__main__':
    create_weather_table()
