from database import SessionLocal, WeatherLog
from sqlalchemy import func

def run_city_report():
    db = SessionLocal()
    try:
        # 1. Search Frequency (SQL: GROUP BY)
        city_counts = db.query(
            WeatherLog.city, 
            func.count(WeatherLog.id)
        ).group_by(WeatherLog.city).all()

        print("--- Search Frequency per City ---")
        for city, count in city_counts:
            print(f"{city}: {count} searches")

        # 2. Hottest City (SQL: ORDER BY ... DESC LIMIT 1)
        hottest_entry = db.query(WeatherLog).order_by(WeatherLog.temperature.desc()).first()

        if hottest_entry:
            print(f"\nHottest search recorded: {hottest_entry.city} at {hottest_entry.temperature}°")

        # 3. Global Stats (SQL: AVG and COUNT)
        avg_temp = db.query(func.avg(WeatherLog.temperature)).scalar()
        total_logs = db.query(func.count(WeatherLog.id)).scalar()

        if avg_temp is not None:
            print(f"Average Temperature: {round(avg_temp, 2)}°")
        print(f"Total Requests across all cities: {total_logs}")

    finally:
        db.close()

if __name__ == "__main__":
    run_city_report()