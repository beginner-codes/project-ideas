# 📈 Stock Checker - Solution Walk Through using Python

[Instructions](/projects/stock-checker.md) | [Solution Code](/solutions/stock-cker.py) | [All Ideas](/README.md)

Here's how we did this one! It's one way to go about it, so be sure to share your solution!

## Getting Started - Stock Checker

There is a little bit of setup required for this one. The first step is to install the required external packages, in the case of this solution it is just `requests`. This can be installed using `pip`.

`pip install requests`

The next step is to register with the service providing the API to get a token, which is required to make requests, and store this in a file. For this solution we have used [IEX Cloud](https://iexcloud.io/).

A lot of APIs will require you to register and get a token from them, this allows them to track/limit usage. Many services have a limited number of requests for free, then you'd have to pay for more.

This token should always be kept private and not shared with anybody, as such it is bad practice to enter these directly into your code incase you accidentally share it or commit it to a version control system such as git.
There are a few ways that this can be done such as using environment variables or storing it in a seperate text file which the program will then read. For this solution we have gone with the latter.

To do this, we create a text file in the same directory as the .py file, for this solution it has simply been named `api.token`. On the first line of this file paste in the token and save the file.

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


**All Done!!!** [Checkout the completed code!](/solutions/conversion-calculator.py)