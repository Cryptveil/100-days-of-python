import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""

user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
        }

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
        "id": "graph1",
        "name": "Coding Graph",
        "unit": "commit",
        "type": "int",
        "color": "ajisai"
        }

headers = {
        "X-USER-TOKEN": TOKEN,
        }

pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_config = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "30",
        }

put_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

put_config = {
        "quantity": "10"
        }

response = requests.delete(url=put_endpoint, headers=headers)
print(response.text)
