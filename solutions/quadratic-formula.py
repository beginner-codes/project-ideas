import math
import textwrap

def quadratic_calculator(a, b, c):
    """
        The actual calculator function that will do the necessary work for a
        correct polynomial expression to work.
    """

    # Checking if a is smaller than 0 if it is teh polynomial is incorrect
    if a < 0:
        return f"Incorrect a value {a} is smaller than 1"

    # If the polynomial is fine we calculate the discrimnant of the expression
    Discrimnant = ((-b)**2 - 4*a*c)

    # Checking if the discrimnant is valid
    if Discrimnant < 0:
        return f"The given Parabola has no real roots, doesnt touch the x-axis. Discrimnant is lower than 0 {Discrimnant}"


    # Here we are calculating the expression by destructuring the roots into the variables x1 and x2
    x1, x2 =  round((-b - math.sqrt(Discrimnant)) / (2*a), 2), round((-b + math.sqrt(Discrimnant)) / (2*a), 2)

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
    roots: {f'{(x1, 0)} and {(x2, 0)}' if x1 != x2 else x1}\n""")



def main():
    solve = "y"
    while solve == "y":
        # Asking for user input 
        a = int(input("Enter your a value ax² + bx + c: "))
        b = int(input("Enter your b value: "))
        c = int(input("Enter your c value: "))

        # Printing the returned value of our function 
        print(quadratic_calculator(a, b, c))
        
        # Prompting the user again if they want to continue solving questions
        solve = input("Do you want to solve another polynomial? [Y]es or [Any other character to quit]: ").lower()
        print("\n")

    print("Ended!")


if __name__ == '__main__':
    main()
