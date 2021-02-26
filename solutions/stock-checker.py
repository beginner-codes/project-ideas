"""Stock Checker

This is a simple command line stock checker that allows the user to enter a symbol and see the latest price.
This solution will make use of the IEX Cloud API."""

import pathlib

import requests


def read_api_token():
    """Read the API token from the "api.token" file and return it"""
    token_file = pathlib.Path(__file__).parent / "api.token"

    with open(token_file) as f:
        token = f.read().strip()

    return token


def get_stock_data(symbol, token):
    """Send a request to the API with the symbol and token. Return the stock data we want:
    Symbol, Company Name, Current Price"""
    url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={token}"
    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)
        return None

    all_stock_data = response.json()
    name = all_stock_data["companyName"]
    symbol = all_stock_data["symbol"]
    current_price = all_stock_data["latestPrice"]

    stock_data = {"name": name, "symbol": symbol, "current_price": current_price}

    return stock_data


def display_stock_data(token):
    """Ask the user to enter a symbol and then display the stock data."""
    symbol = input("Please enter a stock symbol: ")
    stock_data = get_stock_data(symbol, token)

    if stock_data:
        name = stock_data["name"]
        symbol = stock_data["symbol"]
        current_price = stock_data["current_price"]

        print(f"{name} ({symbol}) - Current price: {current_price}")


def main():
    """Repeatedly asks the user to enter a stock symbol until they want to stop."""
    token = read_api_token()

    again = "y"
    while again == "y":
        display_stock_data(token)
        again = input(
            "Would you like to get the price of another stock (Y/N)? "
        ).lower()

    print("Goodbye!")


if __name__ == "__main__":
    main()
