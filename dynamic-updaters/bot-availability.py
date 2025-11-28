import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("STATUSPAGE_API_TOKEN")
URL = "https://api.statuspage.io/v1/pages/swdxbqz393w9/components/h69f0ypjcbqj/uptime"

headers = {
    "Authorization": f"OAuth {API_TOKEN}"
}

res = requests.get(URL, headers=headers)
data = res.json()

uptime = data["uptime_percentage"]

with open("dynamic/AVAILABILITY", "w") as f:
    f.write("Uptime: " + str(uptime) + "%")
