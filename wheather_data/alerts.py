# Check if alert thresholds are breached
def check_alerts(daily_summaries, alert_thresholds):
    alerts = []

    for city, days in daily_summaries.items():
        for date, records in days.items():
            temps = [r['temp'] for r in records]
            if len(temps) >= 2 and all(t > alert_thresholds['temp'] for t in temps[-2:]):
                alerts.append(f"ALERT: High temperature in {city} on {date} exceeded {alert_thresholds['temp']}°C")
    
    return alerts
