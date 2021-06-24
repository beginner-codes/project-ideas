"""Pythagorean Theorom Solver

This is a simple program that calculates the length of a side
of a right-angle triangle."""

from math import sqrt

def pythagorean_theorom_solver(first_num, second_num, side):
    """Check what side it is and perform calcultion based on that."""
    if side == 'c':
        return sqrt(first_num**2 + second_num**2)
    
    try:
        return sqrt(second_num**2 - first_num**2)
    except ValueError:
        opposite_side = "b" if side == "a" else "a"
        return f"{opposite_side} must be shorter than c."
    
def start():
    """Ask for input and run the function to perform calculations."""
    go_on = 'y'
    side_dict = {'a':('b','c'),'b':('a','c'), 'c':('a','b')}
    
    while go_on == 'y':
        side = input("what side do you want to calculate(a,b,c): ")
        side_1,side_2 = side_dict[side]
        length_1 = int(input(f"Enter the length of {side_1} side: "))
        length_2 = int(input(f"Enter the length of {side_2} side: "))
        print(pythagorean_theorom_solver(length_1, length_2, side))
        go_on = input('Press "y" to continue: ')
        
    print("Thanks for playing.")
    
if __name__ == "__main__":
    start()



