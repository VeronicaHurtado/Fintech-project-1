import requests
import os
from constants import GOOGLE_API_DISTANCE_MATRIX
from dotenv import load_dotenv
import json

load_dotenv()

# Set Google API key
google_api_key = os.getenv("GOOGLE_MAPS_API_KEY")


def params_to_query_string(params):
    query_string = ''
    # ToDo: Convert a Dictionary of params to query params
    return query_string


def get_distance(origins, destinations, output_format='json'):
    url = GOOGLE_API_DISTANCE_MATRIX + output_format + '?'

    if not origins or not destinations:
        return 'You need to provide start and destination addresses'

    # Add Key
    url += 'key=' + google_api_key
    url += '&origins=' + origins + '&destinations=' + destinations

    response = requests.get(url)
    data = json.loads(response.text)
    distance_in_metres = data['rows'][0]['elements'][0]['distance']['value']
    distance_in_kilometres = distance_in_metres/1000
    return distance_in_kilometres


# Get fuel consumption/efficiency in Kilometres per litre
def get_fuel_consumption(car_make, car_model):
    # @ToDo: Get actual API for this function
    car_api_url = f"https://example.com/api/car_efficiency?make={car_make}&model={car_model}"
    car_response = requests.get(car_api_url)
    car_data = json.loads(car_response.text)
    try:
        kml = car_data["klm"]
    except KeyError:
        raise ValueError(f"No data found for {car_make} {car_model}.")
    return kml


def get_car_emissions_rate(car_make, car_mode):
    # @ToDo: Use car emissions API to get the emissions rate for a car
    car_emissions_url = "https://example.com/car_emissions_api"
    car_emissions_response = requests.get(car_emissions_url)
    car_emissions_data = json.loads(car_emissions_response.text)
    car_emissions_rate = car_emissions_data["emissions_rate"]
    return car_emissions_rate
