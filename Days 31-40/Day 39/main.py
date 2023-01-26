from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

# Starts from London because this was the asingment
ORIGIN_CITY_IATA = "LON"

# If the sheet is empty, populates it with the airport codes
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.flight_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

# Checks for a specific flight
for destination in sheet_data:
    flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today,
            )

# Twilio message stuff
if flight.price < destination["lowestPrice"]:
    notification_manager.send_sms(
        message=f"Low price alert! Only £{flight.price} to fly from"
        f"{flight.origin_city}-{flight.origin_airport} to "
        f"{flight.destination_city}-{flight.destination_airport},"
        f"from {flight.out_date} to {flight.return_date}."
    )
