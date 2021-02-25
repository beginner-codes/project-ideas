# 🧮 Conversion Calculator - Solution Walk Through using Python

[Instructions](/projects/conversion-calculator.md) | [Solution Code](/solutions/conversion-calculator.py) | [All Ideas](/README.md)

## Getting Started - Temperature Converter

To start off let's get it to convert between Fahrenheit and Celsius. First we need to ask the user if they want to convert from Fahrenheit or Celsius. We'll only look for the first letter and we'll make it case insensitive.
```python
convert_from = input("Would you like to convert from [f]ahrenheit or [c]elsius? ").lower()[0]
```
We've put the first letter inside of braces to highlight that it is what the user needs to input. We then call `lower` on the input to make all uppercase letters lowercase for consistency. Finally, we grab the 0th character from the input since we only want the first letter.

Next we need to get the user to tell us what the temperature is that they want to convert. We want it to be a decimal number, the input we get from the user is a string, so we need to convert it using the `float` function.
```python
temperature = float(input("What is the temperature? "))
```
We got the user's input then passed it to `float` to convert the string that `input` gives to a number.

The next step is to do the correct conversion based on what the user input. For this we need an `if/else` statement. 
```python
if convert_from == "f":
    ... # Convert to celsius from fahrenheit
else:
    ... # Convert to fahrenheit from celsius
```
This will check if `convert_from` is `"f"` and if it's not we assume it's `"c"` and do the celsius conversion.

After this we need to look up what the formulas are to convert between fahrenheit and celsius. F to C is `(temp - 32) * 5 / 9` and C to F is `temp * 9 / 5 + 32`. So we'll add those formulas to the code and have it print out the result.
```python
if convert_from == "f":
    c = (temperature - 32) * 5 / 9
    print(f"{temperature}F is {c:.2f}C")
else:
    f = (temperature - 32) * 5 / 9
    print(f"{temperature}C is {f:.2f}F")
```
We used f-strings so we could insert our variables into the string. For the converted temperature we also used the format expression `.2f` which tells the f-string how to format the variable. The `f` at the end tells it that the variable is a float (number with a decimal), and the `.2` tells it that we want it to have at most 2 numbers after the decimal point.

## Add A Loop

When we run this it works but when it finishes the conversion it exits. Let's add a loop so it keeps asking us to convert more temperatures until we tell it to quit by typing `q`. To do this we need to add a prompt we'll call `choice` and a while loop that checks `choice`.
```python
choice = ""
prompt = "Would you like to continue ([q]uit to stop)? "
while choice != "q":
    choice = input(prompt).lower()[0]
```
This works like our temperature input, it's case insensitive and only checks the first character. When this is run it just prompts the user if they want to continue over and over. The next thing we need to do is put our temperature conversion code into the loop: 
```python
choice = ""
prompt = "Would you like to continue ([q]uit to stop)? "
while choice != "q":
    convert_from = input("Would you like to convert from [f]ahrenheit or [c]elsius? ").lower()[0]
    temperature = float(input("What is the temperature? "))
    if convert_from == "f":
        c = (temperature - 32) * 5 / 9
        print(f"{temperature}F is {c:.2f}C")
    else:
        f = (temperature - 32) * 5 / 9
        print(f"{temperature}C is {f:.2f}F")

    choice = input(prompt).lower()[0]
```
We had to indent the code so it would be inside the while loop, we also put the `choice` input at the end so it would run last before jumping back to the while to check if choice is not `q` and before asking for another temperature to convert.

## Use A Function

We want to add more calculators but there's already a lot of code, so let's start organizing it by putting the temperature calculator into a function. We'll name the function `temperature_converter`.
```python
def temperature_converter():
    convert_from = input("Would you like to convert from [f]ahrenheit or [c]elsius? ").lower()[0]
    temperature = float(input("What is the temperature? "))
    if convert_from == "f":
        c = (temperature - 32) * 5 / 9
        print(f"{temperature}F is {c:.2f}C")
    else:
        f = (temperature - 32) * 5 / 9
        print(f"{temperature}C is {f:.2f}F")
```
Here we've put all the temperature converter code into a function. We can call the function by name to run its code.
```python
choice = ""
prompt = "Would you like to continue ([q]uit to stop)? "
while choice != "q":
    temperature_converter()
    choice = input(prompt).lower()[0]
```
Super simple and makes our loop cleaner!

## Add A Weight Calculator

Now we want to add a weight calculator to convert between pounds and kilograms. This will require the user to choose which calculator they want, so let's start by adding an `if` that checks if the user chose the temperature converter. We can use the existing quit prompt, we'll just need to move it to the top of the loop and change the message.
```python
choice = ""
prompt = "What calculator do you want to use ([t]emperature, [w]eight, [q]uit): "
while choice != "q":
    choice = input(prompt).lower()[0]
    if choice == "t":
        temperature_converter()
```
Now we can add a new function `weight_converter` that asks the user if they want to convert from pounds or kilograms and what the weight is. The formula for the conversion uses a conversion factor of `2.205`, where 1kg is about 2.205 pounds so to convert lbs to kgs we divide by the factor and to convert to lbs we multiply.
```python
def weight_converter():
    conversion_factor = 2.205
    convert_from = input("Would you like to convert from [p]ounds or [k]ilograms? ").lower()[0]
    weight = float(input("What is the weight? "))
    if convert_from == "p":
        kg = weight / conversion_factor
        print(f"{weight}lbs is {kg:.2f}kgs")
    else:
        pounds = weight * conversion_factor
        print(f"{weight}kgs is {pounds:.2f}lbs")
```
This works very similarly to the `temperature_converter` function, we've just changed the formula to use the conversion factor and updated the prompt messages and variable names to make sense.

Now we need to call the weight converter function if the user selects it at the input prompt.
```python
choice = ""
prompt = "What calculator do you want to use ([t]emperature, [w]eight, [q]uit): "
while choice != "q":
    choice = input(prompt).lower()[0]
    if choice == "t":
        temperature_converter()
    elif choice == "w":
        weight_converter()
```
And now we have two calculators working!

## Add A Distance Calculator

This will function nearly identically to the weight converter with a conversion factor of `0.62137119` where we divide miles by the factor to get kilometers and multiply kilometers to get miles. 
```python
def distance_converter():
    conversion_factor = 0.62137119
    convert_from = input("Would you like to convert from [m]iles or [k]ilometers? ").lower()[0]
    distance = float(input("What is the distance? "))
    if convert_from == "m":
        km = distance / conversion_factor
        print(f"{distance} miles is {km:.2f} kilometers")
    else:
        miles = distance * conversion_factor
        print(f"{distance} kilometers is {miles:.2f} miles")
```
And then we add the function call and update the calculator choice prompt.
```python
choice = ""
prompt = "What calculator do you want to use ([d]istance, [t]emperature, [w]eight, [q]uit): "
while choice != "q":
    choice = input(prompt).lower()[0]
    if choice == "t":
        temperature_converter()
    elif choice == "w":
        weight_converter()
    elif choice == "d":
        distance_converter()
```
## Handling Invalid Input

Sometimes a user may make an incorrect choice or enter an invalid number. So let's add some code to handle that. First we'll start with getting the choices (pounds/kilograms, fahrenheit/celsius, miles/kilometers). This will be easiest if we create a new function that loops until the user chooses a valid option. We'll pass this function the prompt we want the user to see along with a list of valid options.
```python
def get_choice(prompt, options):
    choice = input(prompt).lower()[0]
    while choice not in options:
        print(f"'{choice}' is not a valid choice, pick between: {', '.join(options)}")
        choice = input(prompt).lower()[0]

    return choice
```
This will loop so long as choice is not in the options list. It will only check the first character (0th item) and always converts uppercase letters to their lowercase counterparts, similarly to how we did it in the temperature converter. It then returns the choice so we can store it in a variable. Because the validity check is done by the `while` we need to put an input prompt before the `while` and then again at the end of the loop before the code jumps back to the `while`.

Now let's update our `temperature_converter` function to use this new function.
```python
def temperature_converter():
    convert_from = get_choice("Would you like to convert from [f]ahrenheit or [c]elsius? ", ["f", "c"])
    temperature = float(input("What is the temperature? "))
    if convert_from == "f":
        c = (temperature - 32) * 5 / 9
        print(f"{temperature}F is {c:.2f}C")
    else:
        f = (temperature - 32) * 5 / 9
        print(f"{temperature}C is {f:.2f}F")
```
A simple change of just the first line inside the function. We then need to make similar changes to the `weight_converter` and `distance_converter` functions.
```python
convert_from = get_choice("Would you like to convert from [p]ounds or [k]ilograms? ", ["p", "k"])
```
And
```python
convert_from = get_choice("Would you like to convert from [m]iles or [k]ilometers? ", ["m", "k"])
```

Next let's do something similar for getting numbers. We'll only need to give the function the prompt that we want the user to see. The function will then use a `try/except` to check that the input is valid when it's converted from a string to a float.
```python
def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("You need to provide a valid number")
```
This asks the user for a number using the provided prompt. It then tries to convert it to a floating point number like we've been doing. It adds a `try/except` which is watching for a `ValueError` exception, when it detects that error it prints out a message and lets the loop continue to ask the user for another number.

To use this we just need update our function to call `get_number` rather than `input`. We no longer need to call `float` because that is handled inside of the `get_number` function.
```python
def temperature_converter():
    convert_from = get_choice("Would you like to convert from [f]ahrenheit or [c]elsius? ", ["f", "c"])
    temperature = get_number("What is the temperature? ")
    if convert_from == "f":
        c = (temperature - 32) * 5 / 9
        print(f"{temperature}F is {c:.2f}C")
    else:
        f = (temperature - 32) * 5 / 9
        print(f"{temperature}C is {f:.2f}F")
```
And in our other two functions.
```python
weight = get_number("What is the weight? ")
```
And
```python
distance = get_number("What is the distance? ")
```

## Clean Up With A Dictionary

We can clean up the while loop that chooses the calculator by using a dictionary. We can make the dictionary keys the option the user needs to pick and then the values can be the function to use for that calculator. We'll add `q` as `None` because there's no function needed for quiting.
```py
options = {
    "d": distance_converter,
    "t": temperature_converter,
    "w": weight_converter,
    "q": None
}
```
Now we need to update the loop to run the requested calculator.
```python
prompt = "What calculator do you want to use ([d]istance, [t]emperature, [w]eight, [q]uit): "
choice = get_choice(prompt, options)
while choice != "q":
    options[choice]()
    choice = get_choice(prompt, options)
```
We're asking the user for their choice before the loop so it can check if they quit before trying to run the calculators. We similarly prompt for a new choice at the end of the loop so that when it jumps back to the `while` it can again check if the user quit.

## One Last Step

We should move all of our code into a function, this way we can avoid unintended runs and global variables. The loop that chooses which calculator to use is the only code not in a function, so let's move it into a function we'll name `start`.
```python
def start():
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
```
We can run our `start` function by checking the module name to see if it was run and not imported. Every module has a variable `__name__` and when it has been imported this will be the name of the module. However, when the module was passed to Python to be run (for example `python my_module.py`) it will not be the name, instead it will be `"__main__"`. Python does this to indicate that it is the *main* module. So we can use this to run our `start` function only when the python file is run, we just need to put an if at the end of the file to check if the name is `"__main__"`
```python
if __name__ == "__main__":
    start()
```

**All Done!!!**
