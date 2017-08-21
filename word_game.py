import pprint
from string import ascii_uppercase
from random import choice, sample

def word_search_base(width, height):
    """Generate a random grid of letters."""
    
    columns = []
    # 2D list
    for i in range(width):
        columns.append([choice(ascii_uppercase) for j in range(height)])
    return columns

W2E, E2W, N2S, S2N, NW2SE, NE2SW, SW2NE, SE2NW = range(8)

def insert(word, puzzle, x, y, direction=W2E, inplace=True):
    """Insert a word into a puzzle starting at (x, y) going in the
    specified direction.
    
    Returns a list of newly occupied coordinates and the modified
    puzzle.
    
    """
    
    coords = []
    if not inplace:
        new_puzzle = [[j for j in i] for i in puzzle]
    else:
        new_puzzle = puzzle
    if direction == W2E:
        # going right
        i = x
        for char in word:
            if i < 0:
                raise IndexError
            # Prevent weird word wrapping behavior w/ negative indices
            new_puzzle[i][y] = char
            coords.append((i, y))
            i += 1
    elif direction == E2W:
        # going left
        i = x
        for char in word:
            if i < 0:
                raise IndexError
            new_puzzle[i][y] = char
            coords.append((i, y))
            i -= 1
    elif direction == N2S:
        # going down
        i = y
        for char in word:
            if i < 0:
                raise IndexError
            new_puzzle[x][i] = char
            coords.append((x, i))
            i += 1
    elif direction == S2N:
        # going up
        i = y
        for char in word:
            if i < 0:
                raise IndexError
            new_puzzle[x][i] = char
            coords.append((x, i))
            i -= 1
    elif direction == NW2SE:
        # going down and right
        i, j = x, y
        for char in word:
            if i < 0 or j < 0:
                raise IndexError
            new_puzzle[i][j] = char
            coords.append((i, j))
            i += 1
            j += 1
    elif direction == NE2SW:
        # going down and left
        i, j = x, y
        for char in word:
            if i < 0 or j < 0:
                raise IndexError
            new_puzzle[i][j] = char
            coords.append((i, j))
            i -= 1
            j += 1
    elif direction == SW2NE:
        # going up and right
        i, j = x, y
        for char in word:
            if i < 0 or j < 0:
                raise IndexError
            new_puzzle[i][j] = char
            coords.append((i, j))
            i += 1
            j -= 1
    elif direction == SE2NW:
        # going up and left
        i, j = x, y
        for char in word:
            if i < 0 or j < 0:
                raise IndexError
            new_puzzle[i][j] = char
            coords.append((i, j))
            i -= 1
            j -= 1
    return coords, new_puzzle

    
def word_search(width, height, words):
    """Create a word search with the specified words."""
    
    assert width * height > len("".join(words)), \
           "Too many words for a %sx%s puzzle" % (width, height)
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    assert max_length <= width or max_length <= height, \
           "At least one word is too long for a %sx%s puzzle" % (width, height)
    # Make sure there's enough room
    base = word_search_base(width, height)
    occupied = []
    # occupied coordinates
    word_coords = {}
    # {word: (x, y)}
    for word in words:
        word = word.upper()
        while 1:
            direction = choice(range(8))
            x, y = choice(range(width)), choice(range(height))
            # random direction + coords
            try:
                coords, new_puzzle = insert(word, base, x, y,
                                            direction=direction,
                                            inplace=False)
            except IndexError:
                # Word extends beyond the edge of the puzzle
                continue
            else:
                need_retry = False
                if [c for c in coords if c in occupied]:
                    for i, j in coords:
                        if (i, j) in occupied and \
                           base[i][j] != new_puzzle[i][j]:
                            # space conflict
                            need_retry = True
                            break
                if not need_retry:
                    insert(word, base, x, y, direction=direction)
                    occupied += coords
                    word_coords[word] = coords[0]
                    break
    return base, word_coords


def get_dictionary(source):
    """It creates and returns a dictionary that represents
    the valid entries."""

    f = open(source)
    words = [i.upper() for i in f.read().split()]
    words2 = [i for i in words if (len(i)<5 or len(i)<5)]
    words_hide = sample(words2,5)
    return words_hide


if __name__ == "__main__":
    words = get_dictionary("ospd.txt")
    print(words)
    generateWordFindPuzzle(words,5,10,4)
    # for i in words:
    #    pprint.pprint(insert(i,word_search_base(5,5),0,0))