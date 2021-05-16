# ❌⭕ Tic Tac Toe - Solution Walk Through using Python

[Instructions](/projects/tic-tac-toe.md) | [Solution Code](/solutions/tic-tac-toe.py) | [All Ideas](/README.md)

Here's how we did this one! It's one way to go about it, so be sure to share your solution!

## Getting Started - Tic Tac Toe
The first thing we need to do is decide what our board is going to look like. For our solution we are going to go with this. It's simple and allows each location that the player can move in to either contain a space or X or O.
```
 | |
-+-+-
 | |
-+-+-
 | | 
```
Then we need to decide how to store each players move. For this we are going to use a 2 dimensional list. A 1 dimensional list would be simpler to work but we can use some neat tricks with a 2d list!
Let's define the empty board.
```python
board = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]
]
```

## Displaying the board
Now that we know what we want our board to look like and how we are going to store each move, we can start off by printing the board. The board will be printed after each players turn so we will put this in a function so we can easily print the board.
```python
def display_board(board):
    """Print the current state of the board."""
    for i, row in enumerate(board):
        if i != 0:
            print("-+-+-")
        row = "|".join(row)
        print(row)
```
When called this function will take the board as an argument. Then we user `enumerate` to iterate over the list of lists, enumerate is useful when you need both the index and the value at that index.

We only want to print `-+-+-` twice, once before the second row and once before the third row, so we use an `if` statement to make sure we don't print it before the first row.

Then since we want each item in the row to be separated by `|` we can use `join` to build a string for the row and then print it.

Initially this will print the empty board shown in the getting started section but once we add the functionality for a player to be able to make a move it'll print the current state of the board.

## Make a move
Now that we can display the board, we need to actually allow players to make their moves on it.
For this we will simply number each position on the board and ask the user to enter a number.
```
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9
```
### Asking the player to make their move
Since we are going to have to ask multiple times where a player would like to make their move and we want some input validation lets create a function to help us do this.
```python
def ask_player_for_location(player):
    """Ask the player where they would like to use their turn"""
    move = None
    while not move:
        try:
            move = int(input(f"{player} where would you like to go? "))
            if move not in range(1,10):
                move = None
                raise ValueError
        except ValueError:
            print("Please enter a number from 1-9")
    return move
```
We loop while the player hasn't chosen a valid move and use `try/except` to make sure that what the player has entered is an integer. If they don't enter an integer, a `ValueError` is raised by python when we try to convert it to an `int`. We can also check the number is between 1 and 9 by raising our own `ValueError` if it isn't and catch it in the same except.
We then return the location that the player would like to make their move.

### Converting the players move to a  in our board
We need a way of converting the players input of 1 to 9 to a location on our board, which if you remember is a 2d list. This seems like it might be complicated but we can use `divmod` to make our lives way easier.
```python
def player_turn_to_board_location(move):
    """Convert the players move to a board location."""
    move -= 1
    row, column = divmod(move, 3)
    return row, column
```
Since list indexes start at 0 we first need to subtract 1 from the players move so it's in the range of 0-8. Then we can use `divmod` to get our row and column. Here is a link to the [documentation](https://docs.python.org/3/library/functions.html#divmod) but basically what this does is return the quotient and remainder as a tuple of `move` when it is divided by `3`. We use 3 because that's the width of our board. So anything above 3 will move to the next column. Have a play around with this in the REPL to see how it works. 

To give an example of this. If the user input was `5` (for the centre of the board). We subtract `1` to get `4`. Then when we do `divmod(4, 3)` what we get is `(1, 1)` which we can then use to index our 2d list. `board[1][1]` would be the centre of the board.

### Checking the move is valid
Now that the player can make their move and we know where it would go in our board, before we actually add it we need to make sure that it is valid. We have already made sure that the player enters an integer between 1 and 9 so now the only thing left to check is that the location is empty. Let's create a function for this.
```python
def check_valid_move(location, board):
    """Check the players move is valid."""
    row, column = player_turn_to_board_location(location)
    if board[row][column] != " ":
        print("That position is already taken")
        return False
    return True
```
We use the function we created in the previous step to get the `row` and `column` of the `board`. Then we need to check that it an empty space, if it isn't we let the player know that that position is already taken and `return False`. If the position isn't taken, we `return True`. This will be used in the next step to keep asking for input from the player until they enter a valid move.

### Putting it all together and actually making the move
We have our helper functions so now we can actually let the player make their move. We will have `player` and `board` as parameters as we need to know which `player` is actually making a move and it needs to be able to be made on the `board`.
```python
def player_turn(player, board):
    """Ask player to their turn on the board and return the player who will play next."""
    move = ask_player_for_location(player)
    while not check_valid_move(move, board):
        move = ask_player_for_location(player)
    row, column = player_turn_to_board_location(move)
    board[row][column] = player
    display_board(board)
    return board
```
We use our function to get input from the player and valid it. Then we use a while loop to keep asking the player to make a move until they enter one that is allowed.

Then we find out where this should be on our board and set the value at that location to either `X` or `O` depending on which `player`'s turn it is.
Finally we display the board and return it.

## Playing the game

We can print the board and a player is able to make a move, so we should be able to actually play the game now!
```python
def play():
    """Play the game"""
    board = [
        [" ", " ", " "], 
        [" ", " ", " "], 
        [" ", " ", " "]
    ]
    current_player = "X"

    while True:
        board = player_turn(current_player, board)
```
We define our empty board and set the `current_player` to `X` since they will start. Then use a loop to keep asking the player to make a move. But wait! We don't ever actually change the player so it will be `X` taking a turn every time, this isn't what we want to let's create a function to switch the player.

### Switching which players turn it is
We can create a function and pass in the current `player` then use a dictionary to easily swap from `X` to `O` and vice versa, this is a bit cleaner than using `if` statements.
```python
def switch_player(player):
    """Switch the player from X to O or vice versa and return the player"""
    players = {"X": "O", "O": "X"}
    return players[player]
```
So now our `play` function looks like this. We let a player make a move and then we switch to the other player.
```python
def play():
    """Play the game"""
    board = [
        [" ", " ", " "], 
        [" ", " ", " "], 
        [" ", " ", " "]
    ]
    current_player = "X"

    while True:
        board = player_turn(current_player, board)
        current_player = switch_player(current_player)
```
We are definitely getting there now, but this would just run forever, we need to check for a winner of it is a draw.

## Checking for a winner
Let's create a function and pass in the `board` so that we can check if there is a winner or a draw.
Somebody wins when they get 3 in a line. So this could be any row, any column or the two diagonals. A draw would be if the board gets filled without their being a winner.


### Checking rows
Let's start with the easy one, checking if a row is all the same.

```python
def check_for_win(board, player):
    """Check if the game is over."""
    for row in board:
        if all(move == player for move in row):
            return f"{player} is the Winner!"
```
We start by iterating over each row of the board. Then we need to check if every location in the row contains all `X`s or all `O`s. For this we can use python's `all` function. What this will do is return `True` if every item in the iterable is truthy. 
For this we can iterate over every `move` in the `row` and if it is equal to the `player` (either X or O) then that location will be `True`. If they are all equal to `player` then `all` will return `True`.
Then we return a string that we can print later.

*Note that since only the player that just made a move can win on that particular turn, we don't need to check both X and O. We can just check the current player*

### Checking columns
Next let's check the columns. We can use a very similar method to checking the rows by transposing the 2d list.
```python
def check_for_win(board, player):
    ...
    for column in zip(*board):
        if all(move == player for move in column):
            return f"{player} is the Winner!"
```
Using `zip(*board)` is a simple way to transpose the 2d list so the columns become rows, which allows us to use the exact same check as we did for checking the rows.

`*board` will unpack our 2d list, so as an example it would become `['X', 'O', 'X'], ['O', 'O', 'O'], ['O', 'X', 'O']`. Then when these are passed to `zip`, it will take the value from index 0 of each then and group those together, then index 1 and group those together and finally index 2 and group those together. So we would end up with a `zip` object that looks something like `('X', 'O', 'O'), ('O', 'O', 'X'), ('X', 'O', 'O')`. You can read more about zip in the [documentation](https://docs.python.org/3/library/functions.html#zip).

### Checking diagonals
That just leaves checking the diagonals for the winner.
```python
def check_for_win(board, player):
    ...
    if all(board[i][i] == player for i in range(3)):
        return f"{player} is the Winner!"

    if all(board[i][2 - i] == "X" for i in range(3)):
        return f"{player} is the Winner!"
```
For this we use `all` again like we did for the rows and columns, but we use `range` to loop from 0 to 2 and use indexes to access the values on the `board` since the diagonals will be `[0][0]`, `[1][1]`, `[2][2]` and `[0][2]`, `[1][1]`, `[2][0]`.

### Checking for a draw
If nobody has won, the last thing we need to check for is a draw.
```python
    if all(move != " " for row in board for move in row):
        return "Draw!"

    return False
```
We use `all` again but this time we want to look at very location on the board and check that it isn't empty. If all locations aren't `" "` then this will evaluate to `True` and we return a string to be printed later.

Finally if nobody has won and it isn't a draw then `None` is returned to indicate there is no winner at the moment.

### Putting it together
Now that we can check for a winner or a draw, we only want to loop inside our `play` function while there isn't a winner and it isn't a draw.
```python
def play():
    """Play the game"""
    board = [
        [" ", " ", " "], 
        [" ", " ", " "], 
        [" ", " ", " "]
    ]
    current_player = "X"
    winner = None

    while not winner:
        board = player_turn(current_player, board)
        winner = check_for_win(board, current_player)
        current_player = switch_player(current_player)
    print(winner)
```
We add a variable `winner = None` then loop while there is not currently a winner. After each turn we check if there is a winner, then switch the player.
Once there is a winner or is it a draw then the loop will stop and we print `winner` which will be the value of the string that was returned from our `check_for_win` function.

## Finishing up
The game is pretty much done now, but let's make it a bit more user friendly by printing and introduction at the start of the game and add it to our `play` function.

```python
def introduction():
    print(
        """Welcome to tic tac toe!
To make a move, enter the number corresponding to the location as show below
The board and it's playable positions:
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9\n"""
    )

def play():
    """Play the game"""
    board = [
        [" ", " ", " "], 
        [" ", " ", " "], 
        [" ", " ", " "]
    ]
    current_player = "X"
    winner = None

    introduction()
    while not winner:
        board = player_turn(current_player, board)
        winner = check_for_win(board, current_player)
        current_player = switch_player(current_player)
    print(winner)
```

### Finally
The last part is calling our `play` function. We can do this by checking the module name to see if it was run and not imported. Every module has a variable `__name__` and when it has been imported this will be the name of the module. However, when the module was passed to Python to be run (for example `python my_module.py`) it will not be the name, instead it will be `"__main__"`. Python does this to indicate that it is the *main* module. So we can use this to run our `play` function only when the python file is run, we just need to put an if at the end of the file to check if the name is `"__main__"`
```python
if __name__ == "__main__":
    play()
```
**All Done!!!** [Checkout the completed code!](/solutions/tic-tac-toe.py)