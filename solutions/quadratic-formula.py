import cmath
import textwrap
import math

"""
A simple Quadratic Calculator script returning details about a given quadratic equation
"""

def discriminant_calculator(a, b, c):
    return b**2 - 4 * a *c


def round_complex(complex_num):
    return round(complex_num.real, 4) + round(complex_num.imag, 4) * 1j


def quadratic_formula(a, b, discriminant):
    # Two instances of the roots, one is natural roots and the other is complex calculated with cmath
    if discriminant >= 0:
        x1, x2 =  round((-b - math.sqrt(discriminant)) / (2*a), 2), round((-b + math.sqrt(discriminant)) / (2*a), 2)
        return x1, x2 if x1 != x2 else x1

    x1, x2 = round_complex((-b - cmath.sqrt(discriminant)) / (2*a)), round_complex((-b + cmath.sqrt(discriminant)) / (2*a))
    
    return x1, x2


def quadratic_calculator(a, b, c):
    """
    The actual calculator function that will do the necessary work for a
    correct quadratic expression to work.
    """

    discriminant = discriminant_calculator(a, b, c)
    roots = quadratic_formula(a, b, discriminant)
    formatted_equation = format_equation(a, b, c)

    return textwrap.dedent(
        f"""
        {formatted_equation}
        {'_' * len(formatted_equation)}
        Discriminant: {discriminant}
        roots: {f'x₁ = {roots[0]} and x₂ = {roots[1]}' if roots[0] != roots[1] else roots[0]}\n
        """
    )

def format_equation(a, b, c):
    return f"{a}x² {f'+ {b}' if b > 0 else f'- {abs(b)}'}x {f'+ {c}' if c > 0 else f'- {abs(c)}'}"


def main():
    solve = "y"
    while solve == "y":
        print("Quadratic Calculator Enter your equation in standard form ax² + bx + c")
        try:
            a = int(input("Enter your a value: "))
            b = int(input("Enter your b value: "))
            c = int(input("Enter your c value: "))

        except ValueError:
            print("Sorry you entered a value that isnt a number retry!\n")
            continue

        if a == 0:
            print("Sorry but a cannot be 0!\n")
            continue

        print(quadratic_calculator(int(a), int(b), int(c)))
        solve = input("Do you want to solve another polynomial? [Y]es or [Any other character to quit]: ").lower()

    print("Ended!\n")


if __name__ == '__main__':
    main()
