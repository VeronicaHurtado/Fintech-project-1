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

    payload = {}
    headers = {}

    response = requests.get(url)
    data = json.loads(response.text)

    return data['rows'][0]['elements'][0]['distance']['text']
    

