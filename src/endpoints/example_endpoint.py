""" JSON Endpoint Comparision. """

from ..endpoint import Endpoint
from requests import post, get

context = {
    'api_url':"http://ip-api.com/json/"
}

def get_data_from_api(context: dict):
    data = get(context['api_url']).json()
    return data

def process_data(raw_data:dict, context:dict):
    # Do magic here to return a dict with the data that needs to be tracked
    return {
        "tracking-ip":raw_data['query'],
        'isp':raw_data['isp']
    }

endpoint = Endpoint(
    get_data_from_api,
    process_data,
    context
)

EXPORTS = {
    "name":"example-endpoint",
    "type":"endpoint",
    "endpoint": endpoint
}