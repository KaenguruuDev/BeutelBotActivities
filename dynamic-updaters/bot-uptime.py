import os
import requests
from dotenv import load_dotenv

load_dotenv()

def calculate_uptime(uptime_in_ms):
    total_seconds = uptime_in_ms // 1000

    days = total_seconds // 86400
    remaining_after_days = total_seconds % 86400

    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600

    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60

    return f"{days}d {hours:02d}h:{minutes:02d}m"

API_TOKEN = os.getenv("PTERODACTYL_API_TOKEN")
URL = "https://panel.create-n-beyond.de/api/client/servers/ef7c0100/resources"

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Accept': 'Application/vnd.pterodactyl.v1+json'
}

params = {'include': 'allocations,user,node'}

response = requests.get(URL, headers=headers, params=params)
uptime = response.json()["attributes"]["resources"]["uptime"]

with open("dynamic/UPTIME", "w") as f:
    f.write("Uptime: " + calculate_uptime(uptime))
