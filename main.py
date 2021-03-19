from top_stocks import get_data
from stocks import get_price

def main():
    for ticker_symbol, _ in get_data()[:10]:
        print(ticker_symbol, get_price(ticker_symbol))

if __name__ == "__main__":
    main()