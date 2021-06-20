from math import sqrt

def pythagorean_theorom_solver(first_num, second_num, side):
    if side != 'c':
        try:
            return sqrt(second_num**2 - first_num**2)
        except ValueError:
            if side == 'a':
                return "a must be shorter than c."
            return "b must be shorter than c."
    return sqrt(first_num**2 + second_num**2)
    
        
def start():
    go_on = 'y'
    while go_on == 'y':
        side = input("what side do you want to calculate(a,b,c): ")
        side_1 = int(input("Enter the first side: "))
        side_2 = int(input("Enter the second side: "))
        
        print(pythagorean_theorom_solver(side_1, side_2, side))
        
        go_on = input('Press "y" to continue: ')
    print("Thanks for playing.")
if __name__ == "__main__":
    start()



