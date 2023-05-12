import requests
import os

def trigger_uptime_heartbeat(url):
    response = requests.post(url)
    print(response.status_code)

url = os.environ.get('UPTIME_URL')
response = trigger_uptime_heartbeat(url)