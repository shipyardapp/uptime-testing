import requests
import os

def trigger_uptime_heartbeat(url):
    response = requests.post(url)
    return response

trigger_uptime_heartbeat(url)