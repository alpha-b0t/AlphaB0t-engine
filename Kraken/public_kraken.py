import requests


if __name__ == '__main__':
    time_response = requests.get('https://api.kraken.com/0/public/Time')
    status_response = requests.get('https://api.kraken.com/0/public/SystemStatus')
    asset_response = requests.get('https://api.kraken.com/0/public/Assets')
    asset_pair_response = requests.get('https://api.kraken.com/0/public/AssetPairs?pair=XXBTZUSD,XETHXXBT')
    ticker_info_response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    ohlc_response = requests.get('https://api.kraken.com/0/public/OHLC?pair=XBTUSD')
    order_book_response = requests.get('https://api.kraken.com/0/public/Depth?pair=XBTUSD')
    recent_trades_response = requests.get('https://api.kraken.com/0/public/Trades?pair=XBTUSD')
    recent_spreads_repsonse = requests.get('https://api.kraken.com/0/public/Spread?pair=XBTUSD')

    print(time_response.json())
    print(status_response.json())
    print(asset_response.json())
    print(asset_pair_response.json())
    print(ticker_info_response.json())
    print(ohlc_response.json())
    print(order_book_response.json())
    print(recent_trades_response.json())
    print(recent_spreads_repsonse.json())
