from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

from config._config import get_config
from trading_bot.client import get_trading_client

config = get_config()

def get_all_assets():
    trading_client = get_trading_client()

    search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

    assets = trading_client.get_all_assets(search_params)
    return assets

ass = get_all_assets()
print(ass)