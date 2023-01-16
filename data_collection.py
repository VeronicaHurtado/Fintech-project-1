import requests
import os
import pandas as pd
from constants import GOOGLE_API_DISTANCE_MATRIX, GOOGLE_API_PLACE_AUTOCOMPLETE, GOOGLE_API_DIRECTIONS
from constants import NSW_GOV_API_BASE_URL, NSW_GOV_API_ACCESS_TOKEN_PATH
from dotenv import load_dotenv
import json

# Load dotenv and set all keys
load_dotenv()
google_api_key = os.getenv("GOOGLE_MAPS_API_KEY")  # Set Google API key
nsw_gov_api_auth = os.getenv("NSW_GOV_FUEL_API_AUTHORIZATION")  # Set NSW Gov Authorization
nsw_gov_api_key = os.getenv("NSW_GOV_FUEL_API_KEY")  # Set NSW Gov API key


def load_vehicles_df():
    csv_path = "Resources/vehicles.csv" # Setting path from csv
    df = pd.read_csv(csv_path)
    return df


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
    distance_in_kilometres = distance_in_metres / 1000
    # time = data['rows'][0]['elements'][0]['duration']['text']
    # seconds = data['rows'][0]['elements'][0]['duration']['value']

    return distance_in_kilometres


def get_pt_details(origin, destination, output_format='json'):
    url = GOOGLE_API_DIRECTIONS + output_format + '?'

    if not origin or not destination:
        return 'You need to provide start and destination addresses'

    # Add Key
    url += 'key=' + google_api_key
    # Addresses
    url += '&origin=' + origin + '&destination=' + destination
    # Public Transport mode
    url += '&mode=transit'

    response = requests.get(url)
    data = json.loads(response.text)

    # duration = data['']

    print(data)
    # @ToDo: Finish the public transport function


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


def load_lottie(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def get_nsw_gov_token():
    headers = {'Authorization': nsw_gov_api_auth}
    url = NSW_GOV_API_BASE_URL + NSW_GOV_API_ACCESS_TOKEN_PATH
    url += '?grant_type=client_credentials'

    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        return None

    data = json.loads(response.text)
    # @ToDo: Save token and only request a new one upon expiry

    if data['access_token']:
        return data['access_token']

    return False


def get_fuel_price():
    token = get_nsw_gov_token()

    headers = {
        'content-type': "application/json",
        'authorization': 'Bearer ' + token,
        'apikey': nsw_gov_api_key
    }

    url = NSW_GOV_API_BASE_URL + 'FuelPriceCheck/v2/fuel/prices/station/'
    url += 'Bondi'  # Hard-coding station code for POC

    response = requests.request("GET", url, headers=headers)

    print(response)
    # @ToDo: Finish this function


def address_autocomplete(input_string, output_format='json', location='', radius=''):
    url = GOOGLE_API_PLACE_AUTOCOMPLETE + output_format + "?input=" + input_string
    url += "&types=address&radius=500"
    url += "&fields=[address_components]"
    # url += "&fields=[formatted-address]"
    url += '&key=' + google_api_key  # Add Key

    if radius:
        url += "&location=" + location

    if location:
        url += "&location=" + location

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
