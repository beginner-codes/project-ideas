import pathlib
import requests
import pprint
""" 
    This is a simple Weather script that will retrive weather details of a specific place 
    using the OpenWeathermap API.
    link -> https://openweathermap.org/current

"""


def get_api_token():
    """Read the API token from the file contaiing the token"""
    token_file = pathlib.Path(__file__).parent / "api.token"

    with open(token_file) as f:
        token = f.read().strip()

    return token


def get_current_weather(TOKEN, query, unit):
    """
    Retriving from the api with certain querys, as well as returning easier data to work with 
    if the response was a success
    """
    URL = f"https://api.openweathermap.org/data/2.5/weather"

    parameters = {"q" : query, "units" : unit, "appid": TOKEN}

    request = requests.get(URL, params = parameters)

    if request.status_code != 200:
        return None

    response = request.json()
    main = response["main"]
    description = response["weather"][0]["description"]
    wind = response["wind"]

    return {
    "name" : query.title(), 
    "Main" : main,
    "details": description,
    "wind" : wind
    }


def display_current_weather(TOKEN, query, degrees, unit):
    """
    Retrieving the data out of the simplified dictionary,
    and formatting it in the formatted_string
    """

    # Getting the data from the api
    data = get_current_weather(TOKEN, query, unit[0])

    # Retrieving the values from the parsed API data
    wind = data["wind"]
    main = data["Main"]
    name = data["name"]
    details = data["details"]

    temp = main["temp"]
    feels_like = main["feels_like"]
    high, low = main["temp_max"], main["temp_min"]
    humidity = main["humidity"]

    wind_speed = wind["speed"]
    wind_direction = wind["deg"]

    # Entering the values in a nice formatted string

    formatted_text = f"""
    Place: {name}
    {details.title()}
    Currently {temp}{degrees}, feels like {feels_like}{degrees} with a high of {high}{degrees} and a low of {low}{degrees}.
    Humitidy is at {humidity}
    Wind is at a speed of {wind_speed} {unit[1]}
    Direction: {wind_direction}⁰
    """

    print(formatted_text)


def main():
    TOKEN = get_api_token()

    # Setting a imperial and metric measurment dict for the convenience of the user.
    units = {"f": ("imperial", "Mph"), "c":("metric", "Km/h")}

    choice = "y"
    while choice == "y":
        unit_query = input("\nEnter a unit of tempreature [C]elcius, [F]arenheit: ").lower()
        # Retriving the unit of measurment with .get() so no error is thrown
        unit = units.get(unit_query, None)

        if not unit:
            print("Im sorry but that unit of measurment isnt available")
            continue

        city_query = input("\nEnter a city: ")
        print("----------------"+ "-" * len(city_query))

        display_current_weather(TOKEN, city_query, ("⁰" + unit_query), unit)

        choice = input("Do you want to continue getting other weather reports? [Y]es or any other character to quit: ").lower()
    
    print("Done!")


if __name__ == "__main__":
    main()