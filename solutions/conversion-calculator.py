"""Conversion Calculator

This is a simple conversion calculator that allows the user to convert between fahrenheit/celsius, pounds/kilograms, and
miles/kilometers."""


def get_choice(prompt, options):
    """Prompts the user to choose between a selection of options and continues until the user selects a valid option."""
    while (choice := input(prompt).lower()[0]) not in options:
        print(f"'{choice}' is not a valid choice, pick between: {', '.join(options)}")

    return choice


def get_number(prompt):
    """Prompts the user for a floating point number and continues prompting until a valid input is given."""
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("You need to provide a valid number")


def distance_converter():
    """Calculator that asks the user if they'd like to convert from miles or kilometers and then convertrs the distance
    they enter."""
    conversion_factor = 0.62137119
    convert_from = get_choice(
        "Would you like to convert from [m]iles or [k]ilometers? ", ["m", "k"]
    )
    distance = get_number("What is the distance? ")
    if convert_from == "m":
        km = distance / conversion_factor
        print(f"{distance} miles is {km:.2f} kilometers")
    else:
        miles = distance * conversion_factor
        print(f"{distance} kilometers is {miles:.2f} miles")


def temperature_converter():
    """Calculator that asks the user if they'd like to convert from fahrenheit or celsius and then convertrs the
    temperature they enter."""
    convert_from = get_choice(
        "Would you like to convert from [f]ahrenheit or [c]elsius? ", ["f", "c"]
    )
    temperature = get_number("What is the temperature? ")
    if convert_from == "f":
        c = (temperature - 32) * 5 / 9
        print(f"{temperature}F is {c:.2f}C")
    else:
        f = temperature * 9 / 5 + 32
        print(f"{temperature}C is {f:.2f}F")


def weight_converter():
    """Calculator that asks the user if they'd like to convert from pounds or kilograms and then converts the weight
    they enter."""
    conversion_factor = 2.205
    convert_from = get_choice(
        "Would you like to convert from [p]ounds or [k]ilograms? ", ["p", "k"]
    )
    weight = get_number("What is the weight? ")
    if convert_from == "p":
        kg = weight / conversion_factor
        print(f"{weight}lbs is {kg:.2f}kgs")
    else:
        pounds = weight * conversion_factor
        print(f"{weight}kgs is {pounds:.2f}lbs")


def start():
    """Ask the user what calculator they'd like to use and then start the calculator until the user quits."""
    options = {
        "d": distance_converter,
        "t": temperature_converter,
        "w": weight_converter,
        "q": None,
    }
    prompt = "What calculator do you want to use ([d]istance, [t]emperature, [w]eight, [q]uit): "
    choice = get_choice(prompt, options)
    while choice != "q":
        options[choice]()
        choice = get_choice(prompt, options)

    print("Goodbye!")


if __name__ == "__main__":
    start()
