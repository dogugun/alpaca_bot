from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus

from trading_bot.client import get_trading_client



def get_all_open_orders(side):
    trading_client = get_trading_client()
    request_params = GetOrdersRequest(
        status=QueryOrderStatus.OPEN,
        side=side
    )

    # orders that satisfy params
    orders = trading_client.get_orders(filter=request_params)
    return orders

def create_order(symbol, qty, side):
    trading_client = get_trading_client()
    # preparing orders
    market_order_data = MarketOrderRequest(
                        symbol=symbol,#"SPY",
                        qty=qty,
                        side = side,
                        time_in_force=TimeInForce.DAY
                        )
    return market_order_data


def submit_order(order):
    trading_client = get_trading_client()
    order_result = trading_client.submit_order(
                    order_data=order
                   )
    return order_result


def cancel_all_orders():
    trading_client = get_trading_client()
    cancel_statuses = trading_client.cancel_orders()
    return cancel_statuses


# op_res = submit_order(create_sell_order("SPY", 0.023))
# print(op_res)

# res = get_all_open_orders(OrderSide.BUY)
# print(res)

res = cancel_all_orders()
print(res)
