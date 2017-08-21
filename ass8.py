from time import clock
import random
import itertools
from collections import defaultdict


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
            grid[row].append(".")
    return grid


def printGrid(grid):
    # Print the grid to the screen
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            print(grid[row][column], end="")
        print()


def generateDoubleWordSquare(dictionary, num_grid):

    viable_words = [i for i in dictionary if len(i) == num_grid]
    print(len(viable_words))
    grid = createGrid(num_grid,num_grid)
    printGrid(grid)
    
    viable_grid = itertools.permutations(viable_words, num_grid)
    for grid in viable_grid:
        words = ["" for i in range(num_grid)]
        for i in range(num_grid):
            for j in grid:
                words[i] += j[i]
        flag = 0
        for i in words:
            if (i in viable_words):
                flag += 1
            elif (i not in viable_words):
                break
        if flag == len(words):
            break
        else:
            flag = 0
    print(grid, words)

if __name__ == "__main__":
    words = get_dictionary("ospd.txt")
    # puzzle, words_hidden = generateWordFindPuzzle(words, 4, 10, 10)
    # findWords(words, puzzle)
    generateDoubleWordSquare(words, 4)