from config import StrategyConfig # Needed for children of parent class Strategy
import inspect
from constants import CLASS_NAMES

class Strategy():
    # TODO: Finish implementing (along with StrategyConfig in config.py)
    def __init__(self):
        self.classname = self.__class__.__name__
    
    def get_exchange_time(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_exchange_status(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_asset_info(self, asset, aclass):
        raise NotImplementedError("Not Implemented.")
    
    def get_tradable_asset_pairs(self, pair, info):
        raise NotImplementedError("Not Implemented.")
    
    def get_ticker_info(self, pair):
        raise NotImplementedError("Not Implemented.")

    def get_ohlc_data(self, pair, interval, since):
        raise NotImplementedError("Not Implemented.")
    
    def get_order_book(self, pair, count):
        raise NotImplementedError("Not Implemented.")
    
    def get_recent_trades(self, pair, since, count):
        raise NotImplementedError("Not Implemented.")
    
    def get_recent_spreads(self, pair, since):
        raise NotImplementedError("Not Implemented.")
    
    def add_order(self):
        raise NotImplementedError("Not Implemented.")
    
    def add_order_batch(self):
        raise NotImplementedError("Not Implemented.")
    
    def edit_order(self):
        raise NotImplementedError("Not Implemented.")
    
    def cancel_order(self):
        raise NotImplementedError("Not Implemented.")
    
    def cancel_order_batch(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_account_balance(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_extended_balance(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_trade_balance(self, asset):
        raise NotImplementedError("Not Implemented.")
    
    def get_open_orders(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_closed_orders(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_orders_info(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_trades_info(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_trades_history(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_trade_volume(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_holdings_and_bought_price(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_cash_and_equity(self):
        raise NotImplementedError("Not Implemented.")
    
    def get_crypto_holdings_capital(self):
        raise NotImplementedError("Not Implemented.")
    
    @classmethod
    def from_json(cls, json_data):
        # Get the parameters of the __init__ method
        init_params = inspect.signature(cls.__init__).parameters

        # Extract known attributes
        known_attributes = {param for param in init_params if param != 'self'}
        known_data = {k: v for k, v in json_data.items() if k in known_attributes}

        # Extract additional attributes
        additional_data = {k: v for k, v in json_data.items() if k not in known_attributes}

        # Create instance with known attributes
        instance = cls(**known_data)

        # Set additional attributes
        for key, value in additional_data.items():
            if isinstance(value, dict) and 'classname' in value and value['classname'] in CLASS_NAMES:
                exec(f'setattr(instance, key, {value["classname"]}.from_json(value))')
            else:
                setattr(instance, key, value)
        
        return instance