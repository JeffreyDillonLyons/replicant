# Importing the API and instantiating the REST client according to our keys
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = "PK1TAUBD6IUFSBLTPW99"

SECRET_KEY = "yM9xaujDLbF7XvyAsqqywoFak29coigdgnYimGRh"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

account = trading_client.get_account()

#for property_name, value in account:
#  print(f"\"{property_name}\": {value}")account = trading_client.get_account()

market_order_data = MarketOrderRequest(

                    symbol = "BTC/USD",
                    qty = 1,
                    side = OrderSide.BUY,
                    time_in_force = TimeInForce.GTC
                    
                    )

market_order = trading_client.submit_order(market_order_data)

print(market_order)


     




