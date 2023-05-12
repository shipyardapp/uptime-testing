import requests
import os

url = os.environ.get('UPTIME_URL')
response = requests.post(url)
print(response.status_code)
