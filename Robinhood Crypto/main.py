from bot import SpotGridTradingBot
from order import *
from error_queue import ErrorQueue, ErrorQueueLimitExceededError
from dotenv import dotenv_values

def confirm_grids(upper_price, lower_price, level_num, cash):
    print("Please confirm you want the following:")
    for i in range(level_num-1, -1, -1):
        if i == level_num-1:
            print("=============================================")
            print('grid_' + str(i) + ':')
            print('\tprice: $' + str(upper_price - (level_num-1-i)*(upper_price-lower_price)/(level_num-1)))
            print('\tcash: $' + str(cash/level_num))
            print("=============================================")
        else:
            print('grid_' + str(i) + ':')
            print('\tprice: $' + str(upper_price - (level_num-1-i)*(upper_price-lower_price)/(level_num-1)))
            print('\tcash: $' + str(cash/level_num))
            print("=============================================")

    
    response = input("Yes/Y or No/N: ")
    while response not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
        response = input("Yes/Y or No/N: ")
    
    if response in ['Yes', 'yes', 'y', 'Y']:
        return True
    else:
        return False

if __name__ == '__main__':
    env_config = dotenv_values(".env")
    
    config = {
        'crypto': env_config['CRYPTO'],
        'days_to_run': int(env_config['DAYS_TO_RUN']),
        'mode': env_config['MODE'],
        'backtest': {
            'interval': env_config['BACKTEST_INTERVAL'],
            'span': env_config['BACKTEST_SPAN'],
            'bounds': env_config['BACKTEST_BOUNDS'],
        },
        'upper_price': float(env_config['UPPER_PRICE']),
        'lower_price': float(env_config['LOWER_PRICE']),
        'level_num': int(env_config['LEVEL_NUM']),
        'cash': float(env_config['CASH']),
        'loss_threshold': float(env_config['LOSS_THRESHOLD']),
        'loss_percentage': float(env_config['LOSS_PERCENTAGE']),
        'latency_in_sec': float(env_config['LATENCY_IN_SEC']),
        'is_static': bool(env_config['IS_STATIC']),
        'send_to_discord': bool(env_config['SEND_TO_DISCORD']),
        'discord_latency_in_hours': float(env_config['DISCORD_LATENCY_IN_HOURS']),
        'discord_url': env_config['DISCORD_URL'],
        'max_error_count': int(env_config['MAX_ERROR_COUNT']),
        'error_latency_in_sec': float(env_config['ERROR_LATENCY_IN_SEC']),
        'init_buy_error_latency_in_sec': float(env_config['INIT_BUY_ERROR_LATENCY_IN_SEC']),
        'init_buy_error_max_count': int(env_config['INIT_BUY_ERROR_MAX_COUNT']),
        'cancel_orders_upon_exit': env_config['CANCEL_ORDERS_UPON_EXIT']
    }
    
    if confirm_grids(config['upper_price'], config['lower_price'], config['level_num'], config['cash']):
        spot_grid_trader = SpotGridTradingBot(config)
        del env_config, config
        spot_grid_trader.run()
    else:
        del env_config, config
