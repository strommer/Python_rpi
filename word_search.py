from time import clock
import random
 
start = clock()

# Create a grid filled with "." representing a blank
def createGrid(height, width):
    grid=[]
    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(".")
    return grid
         
# Print the grid to the screen        
def printGrid(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            print(grid[row][column],end="")
        print()
         

def tryToPlaceWord(grid,word):
    # Selecting the direction for the placement of the word
    direction=random.randrange(0,8)
    if( direction == 0 ):
        x_change=-1
        y_change=-1
    if( direction == 1 ):
        x_change=0
        y_change=1
    if( direction == 2 ):
        x_change=1
        y_change=-1
    if( direction == 3 ):
        x_change=1
        y_change=0
    if( direction == 4 ):
        x_change=1
        y_change=1
    if( direction == 5 ):
        x_change=0
        y_change=1
    if( direction == 6 ):
        x_change=-1
        y_change=1
    if( direction == 7 ):
        x_change=-1
        y_change=0
         
    # Find the length and height of the grid
    height=len(grid)
    width=len(grid[0])
     
    # Create a random start point
    column = random.randrange(width)
    row = random.randrange(height)
     
    # Check to make sure  the word won't run off the edge of the grid.
    # If it does, return False. We failed.
    if( x_change < 0 and column < len(word) ):
        return False
    if( x_change > 0 and column > width - len(word) ):
        return False
    if( y_change < 0 and row < len(word) ):
        return False
    if( y_change > 0 and row > height - len(word) ):
        return False
     
    # Now check to make sure there isn't another letter in our way
    current_column = column
    current_row = row
    for letter in word:
        # Make sure it is blank, or already the correct letter.
        if grid[current_row][current_column]==letter or grid[current_row][current_column]=='.':
            current_row += y_change
            current_column += x_change
        else:
            # In case a letter is already present return false
            return False
         
  # Actual placement of the words
    current_column = column
    current_row = row
    for letter in word:
        grid[current_row][current_column]=letter
        current_row += y_change
        current_column += x_change
    return True
 
# Loop for checking whether the word can be placed succefully in the grid
def placeWord(grid,word):
    success=False
    start = clock()

    while not(success):
        success=tryToPlaceWord(grid,word)
        end = clock() - start
        if (end > 3):
            print ('"' + word +'" could not be placed in the grid!! Use a bigger grid size or Lower the number of words')
            break

# Create an empty grid   
grid = createGrid(15,15)
 
# Place some words
placeWord(grid,"pandabear")
placeWord(grid,"fish")
placeWord(grid,"snake")
placeWord(grid,"porcupine")
placeWord(grid,"dog")
placeWord(grid,"cat")
placeWord(grid,"tiger")
placeWord(grid,"bird")
placeWord(grid,"alligator")
placeWord(grid,"ant")
placeWord(grid,"camel")
placeWord(grid,"dolphin")
 
# Print it out
printGrid(grid)
