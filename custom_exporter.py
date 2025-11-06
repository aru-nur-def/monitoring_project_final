from prometheus_client import start_http_server, Gauge
import random
import time

temperature_gauge = Gauge('custom_temperature_celsius', 'Random temperature in Celsius')
humidity_gauge = Gauge('custom_humidity_percent', 'Random humidity in percent')

if __name__ == "__main__":
    start_http_server(8000)
    print("✅ Custom exporter запущен на http://localhost:8000/metrics")

    while True:
        temp = random.uniform(31.0, 35.0)
        humidity = random.uniform(30.0, 80.0)
        temperature_gauge.set(temp)
        humidity_gauge.set(humidity)
        print(f"📊 Temperature={temp:.2f}°C | Humidity={humidity:.1f}%")
        time.sleep(5)
