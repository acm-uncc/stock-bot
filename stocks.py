from yfinance import Ticker

def get_price(ticker_symbol):
  stock = Ticker(ticker_symbol)
  data = stock.info
  return {'ask': data["ask"], 'bid': data["bid"]}

