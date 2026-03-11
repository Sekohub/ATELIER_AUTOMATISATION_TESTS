import requests
import time

API_URL = "https://api.rainviewer.com/public/weather-maps.json"

def call_api():

    start = time.time()

    r = requests.get(API_URL, timeout=3)

    latency = time.time() - start

    return {
        "status": r.status_code,
        "latency": latency,
        "json": r.json(),
        "headers": r.headers
    }
