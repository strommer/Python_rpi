from pprint import pprint
from collections import defaultdict
import string
import math

def get_dictionary(source):
    """It creates and returns a dictionary that represents
    the valid entries."""

    f = open(source)
    words = [i.upper() for i in f.read().split()]
    return words


def createGrid(height, width):
    # Create a grid filled with "." representing a blank
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(["."])
    return grid


def printGrid(grid):
    # Print the grid to the screen
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            print(grid[row][column], end="")
        print()


words = get_dictionary("ospd.txt")
viable_words = [i for i in words if len(i) == 2]
print(len(viable_words))

def new_list(list1, string1):
    if string1 != 0:
        viable_words = [i for i in list1 if(i[:len(string1)] == string1)]
    else:
        viable_words = list1
    return(viable_words)

grid = createGrid(4,4)
printGrid(grid)

global status
def place_grid(grid, word_list, substring_check, status, flag = 0):
    if status == 1:
        pass
    else:
        new_viable = new_list(word_list, substring_check)
        if (int(flag/2) == len(word)):
            word_check = ["".join(grid[k][len(word)-1]) for k in len(range(word))]
            if(word_check in new_viable):
                status = 1
                return (grid, True)
            else:
                return (grid, False)
        if (flag%2 == 0):
            #even flags are columns
            if (len(new_viable) != 0):
                for new_word in new_viable:
                    for i in range(len(new_word)):
                        grid[math.floor(flag/2)][i] = new_word[i]
                    place_grid(grid, new_viable, grid[0],status, flag+1)
            else:
                return(grid,False)
        if (flag%2 == 1):
            #odd flags are rows
            if (len(new_viable) != 0):
                for new_word in new_viable:
                    for j in new_word:
                        grid[j][math.floor(flag/2)] = new_word[j]
                    place_grid(grid, new_viable, grid[0],status, flag+1)
            else:
                return(grid, False)
status = 0

for word in viable_words:
    for i in range(len(word)):
        print(word[i])
        grid[0][i] = word[i]
    place_grid(grid, viable_words, status,grid[0])


printGrid(grid)
