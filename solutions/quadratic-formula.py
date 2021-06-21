import cmath
import textwrap
import math

"""
A simple Quadratic Calculator script returning details about a given polynomial
"""

def discrimnant(a, b, c):
    return ((-b)**2 - 4*a*c)

def quadartic_formula(a, b, Discrimnant):
    # Two instances of the roots, one is natural roots and the other is complex calculated with cmath
    if Discrimnant >= 0:
        x1, x2 =  round((-b - math.sqrt(Discrimnant)) / (2*a), 2), round((-b + math.sqrt(Discrimnant)) / (2*a), 2)
        return x1, x2 if x1 != x2 else x1

    x1, x2 = (-b - cmath.sqrt(Discrimnant)) / (2*a), (-b + cmath.sqrt(Discrimnant)) / (2*a)
    return x1, x2

def quadratic_calculator(a, b, c):
    """
        The actual calculator function that will do the necessary work for a
        correct polynomial expression to work.
    """

    Discrimnant = discrimnant(a, b, c)
    roots = quadartic_formula(a, b, Discrimnant)
        
    # Formatting the equation into a nice string for the user to see.
    formatted_equation = f"{a}x² {f'+ {b}' if b > 0 else f'- {abs(b)}'}x {f'+ {c}' if c > 0 else f'- {abs(c)}'}"

    """
    Returning the final answer in a nice format with the Discrimnant and roots. 
    The conditional ternarys inside will check if it has one root or two.
    """
    return textwrap.dedent(f"""
    {formatted_equation}
    {'_'*len(formatted_equation)}
    Discrimnant: {Discrimnant}
    roots: {f'x1 = {roots[0]} and x2 = {roots[1]}' if roots[0] != roots[1] else roots[0]}\n""")

def valid_input(a, b, c):
    return all(map(str.isnumeric, (a, b, c)))
    
def main():
    solve = "y"
    while solve == "y":
        # Asking for user input and checking if it is all of type int before conversion
        a = input("Enter your a value ax² + bx + c: ")
        b = input("Enter your b value: ")
        c = input("Enter your c value: ")

        if not valid_input(a, b, c):
            print("Sorry you entered a value that isnt a number retry!\n")
            continue

        # Printing the returned value of our function 
        print(quadratic_calculator(int(a), int(b), int(c)))
        
        # Prompting the user again if they want to continue solving questions
        solve = input("Do you want to solve another polynomial? [Y]es or [Any other character to quit]: ").lower()

    print("Ended!")


if __name__ == '__main__':
    main()
