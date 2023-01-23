import requests

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "0e30afb40ba29f432efe6584ffe444a7"

weather_params = {
        "lat": -16.694002,
        "lon": -49.273652,
        "appid": api_key,
        }

response = requests.get(OWM_Endpoint, params=weather_params)

