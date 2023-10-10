from bot import GridTradingBot
from order import *
from error_queue import ErrorQueue, ErrorQueueLimitExceededError
from config import Config
from helpers import confirm_grids

if __name__ == '__main__':
    config = Config()
    
    if confirm_grids(config['upper_price'], config['lower_price'], config['level_num'], config['cash']):
        grid_trader = GridTradingBot(config.config)
        del config
        grid_trader.run()
    else:
        del config
