from math import sqrt

def pythagorean_theorom_solver(first_num, second_num, side):
    if side == 'a':
        try:
            return sqrt(second_num**2 - first_num**2)
        except ValueError:
            return "b must be smaller than c."
    if side == 'b':
        try:
            return sqrt(second_num**2 - first_num**2)
        except ValueError:
            return "a must be smaller than c."
    if side == 'c':
        return sqrt(first_num**2 + second_num**2)
    
        

go_on = 'y'

while go_on == 'y':
    side = input("what side do you want to calculate(a,b,c): ")
    if side == 'a':
        side_b = int(input("Enter the first side: "))
        side_c = int(input("Enter the second side: "))
        print(pythagorean_theorom_solver(side_b, side_c, side))

    if side == 'b':
        side_a = int(input("Enter the first side: "))
        side_c = int(input("Enter the second side: "))
        print(pythagorean_theorom_solver(side_a, side_c, side))

    if side == 'c':
        side_b = int(input("Enter the first side: "))
        side_c = int(input("Enter the second side: "))
        print(pythagorean_theorom_solver(side_b, side_c, side))
    go_on = input('Press "y" to continue: ')
    
print("Thanks for playing.")



