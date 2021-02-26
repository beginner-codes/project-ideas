# 📈 Stock Checker - Solution Walk Through using Python

[Instructions](/projects/stock-checker.md) | [Solution Code](/solutions/stock-cker.py) | [All Ideas](/README.md)

Here's how we did this one! It's one way to go about it, so be sure to share your solution!

## Getting Started - Stock Checker

### Prerequisite

There is a little bit of setup required for this one. The first step is to install the required external packages, in the case of this solution it is just `requests`. This can be installed using `pip`.

`pip install requests`

The next step is to register with the service providing the API to get a token, which is required to make requests, and store this in a file. For this solution we have used [IEX Cloud](https://iexcloud.io/).

A lot of APIs will require you to register and get a token from them, this allows them to track/limit usage. Many services have a limited number of requests for free, then you'd have to pay for more.

This token should always be kept private and not shared with anybody, as such it is bad practice to enter these directly into your code incase you accidentally share it or commit it to a version control system such as git.
There are a few ways that this can be done such as using environment variables or storing it in a seperate text file which the program will then read. For this solution we have gone with the latter.

To do this, we create a text file in the same directory as the .py file, for this solution it has simply been named `api.token`. On the first line of this file paste in the token and save the file.

### Imports
We import both `pathlib` and `requests`. `pathlib` comes bundled with python and we will use it for reading the api.token file in the next step. `requests` as mentioned previously will be used to make the request to the API.

```py
import pathlib
import requests
```

## Read the token

Since we know that the API token will be required for all requests a sensible start would be to read this from the file.
```python 
def read_api_token():
    """Read the API token from the "api.token" file and return it"""
    token_file = pathlib.Path(__file__).parent / "api.token"

    with open(token_file) as f:
        token = f.read().strip()

    return token
```
The `pathlib` library has been used here as it provides a clean way of ensuring that the program is always looking in the correct place for our `api.token` file. 
```python
pathlib.Path(__file__).parent
```
This will return the folder which the current python file is located in. As an example this might be `C:\Users\User1\Projects\`.

The `/ "api.token"` at the end simply appends the file name to this so we get the full path, in the case of our example this would be `C:\Users\User1\Projects\api.token`

We can then open the file and read from it. `strip()` is used to make sure any whitespace or newline characters are removed and we just get the token.

The token is then returned. We will call this function later in our program when we need the token.

## Make the request to the API

Now that we can read the token, we are able to make the request to the API. Let's create a function for this takes a couple of parameters `symbol` and `token`. We will get the `symbol` from the user a little later and the `token` will come from our `read_api_token` function.

```python
def get_stock_data(symbol, token):
    """Send a request to the API with the symbol and token. Return the stock data we want:
    Symbol, Company Name, Current Price"""
    url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={token}"
    response = requests.get(url)
```

The next thing we do is build up the URL. To get the information that we want we will use the `quote` endpoint. All APIs are different, the only way to know what the format of the url should be is to read the documentation. In the case of IEX Cloud this is the format for the URL. You can read more in the [documentation](https://iexcloud.io/docs/api/#quote). We use an f-string to substitute in the `symbol` we want and our `token`.

Now that we have the url we make a GET request using `requests.get()` and pass in the `url`. This will return a `response`.

### Check the response

```python
def get_stock_data(symbol, token):
    ...
    if response.status_code != 200:
        print(response.text)
        return None
```
After that is a bit of error handling. We want to check the status code of the response to ensure that it was successful. A code of 200 means that is was indeed successfully. There are many other codes that could be returned for different reasons, which can be read about [here](https://iexcloud.io/docs/api/#error-codes).

If the request is not successful, we can print responses text which will contain the error that the API returned, so we don't have to write our own system - neat! We then `return` since we don't want to continue with the rest of the function if there was an error.

### Parse the response
Many APIs will return what is called JSON. This is a widely adopted data format for transfering data. Thankfully the `requests` package has a handy way to convert JSON to a format we can easily work with in python. In this instance, it will become a python dictionary so we can deal with it as such.

```py
def get_stock_data(symbol, token):
    ...
    all_stock_data = response.json()
    name = all_stock_data["companyName"]
    symbol = all_stock_data["symbol"]
    current_price = all_stock_data["latestPrice"]
```
`response.json()` will return a dictionary containing all the data from the response. You can see all the possible attributes in the [documentation](https://iexcloud.io/docs/api/#quote). However for the purposes of this program, we are only interested in three pieces of information. The `companyName`, the `symbol` and it's `latestPrice`. As this is now a python dictionary they can be accessed like any other value in a dictionary.

This information gets stored in variables and then we build our own dictionary & return it for use later in the program.
```py
def get_stock_data(symbol, token):
    ...
    stock_data = {"name": name, "symbol": symbol, "current_price": current_price}

    return stock_data
```

**All Done!!!** [Checkout the completed code!](/solutions/conversion-calculator.py)