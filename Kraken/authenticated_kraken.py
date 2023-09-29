import time
import os
import requests
from authentication import get_kraken_signature

# Read Kraken API key and secret stored in environment variables
api_url = "https://api.kraken.com"
api_key = os.environ['KRAKEN_API_KEY']
api_sec = os.environ['KRAKEN_API_SEC']

# Attaches auth headers and returns results of a POST request
def kraken_authenticated_request(uri_path, data, api_key, api_sec):
    headers = {}
    
    headers['API-Key'] = api_key
    
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)         

    req = requests.post(
        url=(api_url + uri_path),
        headers=headers,
        data=data
    )

    return req

def fetch_nonce():
    return str(int(1000*time.time()))

# Construct the request and print the result
resp = kraken_authenticated_request(
    uri_path='/0/private/TradeBalance',
    data={
        "nonce": fetch_nonce(),
        "asset": "USD"
    },
    api_key=api_key,
    api_sec=api_sec
)

print(resp.json())
