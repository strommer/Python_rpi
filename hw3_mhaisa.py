from time import clock
import random
import itertools
from collections import defaultdict

# Get the list of the words form the given source


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


def direction_return(direction):
    direction_list = [(-1, -1), (0, 1), (1, -1), (
        1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    return direction_list[direction]


def tryToPlaceWord(grid, word):
    # Selecting the direction for the placement of the word
    direction = random.randrange(0, 8)
    x_change, y_change = direction_return(direction)

    # Find the length and height of the grid
    height = len(grid)
    width = len(grid[0])

    # Create a random start point
    column = random.randrange(width)
    row = random.randrange(height)

    # Check to make sure  the word won't run off the edge of the grid.
    # If it does, return False. We failed.
    if(x_change < 0 and column < len(word)):
        return False
    if(x_change > 0 and column > width - len(word)):
        return False
    if(y_change < 0 and row < len(word)):
        return False
    if(y_change > 0 and row > height - len(word)):
        return False

    # Now check to make sure there isn't another letter in our way
    current_column = column
    current_row = row
    for letter in word:
        # Make sure it is blank, or already the correct letter.
        if (grid[current_row][current_column] == letter
                or grid[current_row][current_column] == '.'):
            current_row += y_change
            current_column += x_change
        else:
            # In case a letter is already present return false
            return False

  # Actual placement of the words
    current_column = column
    current_row = row
    for letter in word:
        grid[current_row][current_column] = letter
        current_row += y_change
        current_column += x_change
    return True


def placeWord(grid, word):
    # Loop for checking whether the word can be placed succefully in the grid
    success = False
    start = clock()

    while not(success):
        success = tryToPlaceWord(grid, word)
        end = clock() - start
        if (end > 3):
            print(
                '"' + word + '" could not be placed in the grid!! \
                Use a bigger grid size or Lower the number of words')
            break


def generateWordFindPuzzle(dictionary, num_words, num_rows, num_cols):

    words = [i for i in dictionary if (len(i) < num_rows or len(i) < num_cols)]
    words_hide = random.sample(words, num_words)
    words_hide.sort(key=lambda w: len(w))
    # Create an empty grid
    grid = createGrid(num_rows, num_cols)

    for word in words_hide:
        placeWord(grid, word)

    puzzle = ''
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (grid[x][y] == '.'):
                grid[x][y] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            puzzle += grid[x][y]
        puzzle += '\\n'

    return (puzzle[:-2], words_hide)


def check_word(grid, direction, x, y, height, width, word):

    x_change, y_change = direction_return(direction)

    column = x
    row = y

    # Check to make sure  the word won't run off the edge of the grid.
    # If it does, return False. We failed.
    if(x_change < 0 and column < len(word)):
        return False
    if(x_change > 0 and column > width - len(word)):
        return False
    if(y_change < 0 and row < len(word)):
        return False
    if(y_change > 0 and row > height - len(word)):
        return False

    # Now check to make sure there isn't another letter in our way
    current_column = column
    current_row = row
    for letter in word:
        # Make sure it is blank, or already the correct letter.
        if (grid[current_row][current_column] == letter):
            current_row += y_change
            current_column += x_change
        else:
            # In case a letter is already present return false
            return False
    return True


def findWords(dictionary, puzzle):

    grid2 = puzzle.split('\\n')
    start_pos = defaultdict(list)

    height = len(grid2)
    width = len(grid2[0])

    for i in range(height):
        for j in range(width):
            start_pos[grid2[i][j]].append((i, j))

    words2find = [i for i in dictionary if (len(i) < height or len(i) < width)]

    words_found = []
    for word in words2find:
        if word[0] in start_pos:
            starts = start_pos[word[0]]
            for co_x, co_y in starts:
                if (word not in words_found):
                    for direction in range(8):
                        success_check = check_word(
                            grid2, direction, co_y, co_x, height, width, word)
                        if (success_check and word not in words_found):
                            words_found.append(word)
                            break
                        success_check = False

    return(words_found)


def generateDoubleWordSquare(dictionary, num_grid):

    viable_words = [i for i in dictionary if len(i) == num_grid]
    print(len(viable_words))
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
    # print(findWords(words, puzzle))
    generateDoubleWordSquare(words, 3)
