from replit import db

from stocks import get_price

class InsufficientFunds(Exception):
    """ Insufficient funds for this transaction. """

class InsufficientStocks(Exception):
    """ Insufficient stocks for this transaction. """

class Wallet:
    def __init__(self, name):
        self.name = name
        self.id = f"wallet_{name}"

    @property
    def value(self):
        return db.setdefault(self.id, 0)
    
    @value.setter
    def value(self, amount):
        
        db.setdefault(self.id, amount)

    def buy_stock(self, ticker_symbol, amount):
        total_price = get_price(ticker_symbol)["ask"] * amount
        if total_price > self.value:
            raise InsufficientFunds(f"Not enough funds to purchase {amount} {ticker_symbol} for {total_price}")
        
        self.value -= total_price

        db_name = f"{self.id}_{ticker_symbol}"
        db.setdefault(db_name, 0)
        
        db[db_name] += amount

        return db[db_name]

    
    def sell_stock(self, ticker_symbol, amount):
        total_gain = get_price(ticker_symbol)["bid"] * amount
        db_name = f"{self.id}_{ticker_symbol}"

        current_stock_count = db.setdefault(db_name, 0)
        if amount < current_stock_count:
            raise InsufficientFunds(f"Not enough stocks to purchase {ticker_symbol}")

        db[db_name] -= amount
        self.value += total_gain
      
        return db[db_name]


if __name__ == "__main__":
    # Tests

    wallet = Wallet("foo")


    gmc_price = get_price("AMC")
    buy, sell = gmc_price['ask'], gmc_price['bid']

    start = buy * 10
    wallet.value = start
    cost = buy * 5

    wallet.buy_stock("GMC", 5)

    assert wallet.value == start - cost, "Wallet cash didn't go down"
