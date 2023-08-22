from datetime import datetime

from alpaca.data import StockLatestQuoteRequest, StockBarsRequest, TimeFrame

from trading_bot.client import get_stock_data_client


def get_latest_quote_data(ticker_list: list):
    client = get_stock_data_client()

    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=ticker_list)

    latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)
    return latest_multisymbol_quotes


def get_latest_quote_data(ticker):
    client = get_stock_data_client()

    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=ticker)

    latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)
    return latest_multisymbol_quotes


def get_historical_bar_data(ticker_list: list, start_date, end_date, time_frame = TimeFrame.Day):
    client = get_stock_data_client()

    request_params = StockBarsRequest(
        symbol_or_symbols=ticker_list,
        timeframe=time_frame,
        start=start_date,
        end=end_date
    )

    bars = client.get_stock_bars(request_params)
    return bars


def get_historical_bar_data(ticker, start_date, end_date, time_frame = TimeFrame.Day):
    client = get_stock_data_client()

    request_params = StockBarsRequest(
        symbol_or_symbols=ticker,
        timeframe=time_frame,
        start=start_date,
        end=end_date
    )

    bars = client.get_stock_bars(request_params)
    return bars



res = get_historical_bar_data("SPY")
print(res)