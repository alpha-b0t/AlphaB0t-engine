from RobinhoodCrypto.grid_bot import GRIDBot
from config import GRIDBotConfig
from RobinhoodCrypto.helpers import confirm_grids

if __name__ == '__main__':
    config = GRIDBotConfig()
    
    if confirm_grids(config.upper_price, config.lower_price, config.level_num, config.cash):
        grid_trader = GRIDBot(config)

        del config

        # grid_trader.start()

        backtest_results = grid_trader.backtest(grid_trader.crypto)
        print("backtesting results:")
        print(backtest_results)
        grid_trader.logout()
    else:
        del config