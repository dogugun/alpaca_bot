from alpaca.data import StockHistoricalDataClient
from alpaca.trading import TradingClient

from config._config import get_config

config = get_config()

def get_trading_client():
    trading_client = TradingClient(config.Api.apca_api_key_id, config.Api.apca_api_secret_key)
    return trading_client

def get_stock_data_client():
    stock_client = StockHistoricalDataClient(config.Api.apca_api_key_id, config.Api.apca_api_secret_key)
    return stock_client
