# ICP2
print('Program to show Game Board')


def board_draw(height, width):
    # Initialising Board Parameter
    board = ""
    # Iterating the boardSize using range function
    for ran in range(height):
        # In the Loop, forming the Horizontal and Vertical Lines as shown below
        board = board+" ---" * (width) + "\n" + "|   " * (int(width)) + "|\n"
    # Finally, adding the Horizontal lines at the end based on the width
    board = board+" ---" * (int(width)) + "\n"
    return board


# Getting Inputs from the User
heightInput = int(input("Enter the height of the board: "))
widthInput = int(input("Enter the width of the board: "))

# Calling a function to show the Game Board based on height and width
print(board_draw(heightInput, widthInput))
