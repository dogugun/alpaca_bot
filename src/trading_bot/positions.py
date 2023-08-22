from alpaca.trading.client import TradingClient

from trading_bot.client import get_trading_client


def get_all_positions():
    trading_client = get_trading_client()
    all_positions = trading_client.get_all_positions()
    return all_positions


def close_all_positions():
    trading_client = get_trading_client()
    res = trading_client.close_all_positions(cancel_orders=True)
    return res
