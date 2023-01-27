import requests

SHEET_ENDPOINT = ""


class DataManager:
    """Does all the spreadsheet manipulation"""

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        result = response.json()
        self.destination_data = result["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                    "price": {
                        "iataCode": city["iataCode"]
                        }
                    }
            response = requests.put(
                                    url=f"{SHEET_ENDPOINT}/{city['id']}",
                                    json=new_data
                                    )
            print(response.text)
