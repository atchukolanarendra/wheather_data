import sqlite3
import matplotlib.pyplot as plt

def visualize_summary():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT city, AVG(temp), MAX(temp), MIN(temp)
                      FROM weather_data
                      WHERE timestamp >= strftime('%s', 'now', '-1 day')
                      GROUP BY city''')
    
    data = cursor.fetchall()
    conn.close()

    cities = [row[0] for row in data]
    avg_temps = [row[1] for row in data]
    max_temps = [row[2] for row in data]
    min_temps = [row[3] for row in data]

    plt.plot(cities, avg_temps, label='Avg Temp', marker='o')
    plt.plot(cities, max_temps, label='Max Temp', marker='o')
    plt.plot(cities, min_temps, label='Min Temp', marker='o')

    plt.title('Daily Weather Summary')
    plt.xlabel('City')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()

# Call this to visualize
# visualize_summary()
