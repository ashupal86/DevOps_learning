import requests
import random
import time
routes = [
    "/health",
    "/login",
    "/logout",
    "/data",
    "/status",
    "/"
]
base_url = "http://localhost:8080"
while True:
    route = random.choice(routes)
    response = requests.get(base_url + route)
    print(f"Request to {route}: {response.status_code} - {response.text}")
    time.sleep(5)
