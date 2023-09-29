import requests

KRAKEN_API_BASE_URL = 'https://api.kraken.com'

def kraken_public_request(uri_path, query_parameters={}):
    url = KRAKEN_API_BASE_URL + uri_path

    if query_parameters != {}:
        url += '?'
        key_count = 0
        for key in query_parameters.keys():
            if key_count != 0:
                url += '&'
            
            url += f"{key}={query_parameters[key]}"
            key_count += 1
    
    response = requests.get(url)
    return response

# Fetch time information
time_response = kraken_public_request('/0/public/Time')

# Fetch system status
status_response = kraken_public_request('/0/public/SystemStatus')

# Fetch asset information
asset_response = kraken_public_request('/0/public/Assets')

asset_pair_response = kraken_public_request('/0/public/AssetPairs', {'pair': 'XXBTZUSD,XETHXXBT'})
ticker_info_response = kraken_public_request('/0/public/Ticker', {'pair': 'XBTUSD'})
ohlc_response = kraken_public_request('/0/public/OHLC', {'pair': 'XBTUSD'})
order_book_response = kraken_public_request('/0/public/Depth', {'pair': 'XBTUSD'})
recent_trades_response = kraken_public_request('/0/public/Trades', {'pair': 'XBTUSD', 'count': '1'})
recent_spreads_repsonse = kraken_public_request('/0/public/Spread', {'pair': 'XBTUSD'})
