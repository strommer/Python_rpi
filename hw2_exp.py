import sys
import requests
import os
import subprocess
from random import choice
import collections


def get_dictionary(source, type_, single_word=True):
    """It creates and returns a dictionary that represents
    the valid entries."""

    if(type_ == 'file'):
        f = open(source)
        if(single_word is True):
            words = f.read().split()
        if(single_word is False):
            words = [word.strip('\n') for word in f.readlines()]
        return words
    if(type_ == 'url'):
        f = requests.get(source).text
        if(single_word is True):
            words = f.split()
            return words
        else:
            words = f.split('\n')
            return words
    if(type_ == 'text'):
        if(single_word is True):
            words = source.split()
            return words
        else:
            return [source]


def display(current_word, current_misses):
    """Displays the current state of the game."""
    HANGMAN_STATE = ["""
    +---------
    |       |
    |
    |
    |
    |
    +---------
    """, """
    +---------
    |       |
    |       O
    |
    |
    |
    +---------
    """, """
    +---------
    |       |
    |       O
    |       |
    |
    |
    +---------
    """, """
    +---------
    |       |
    |       O
    |      \|
    |
    |
    +---------
    """, """
    +---------
    |       |
    |       O
    |      \|/
    |
    |
    +---------
    """, """
    +---------
    |       |
    |       O
    |      \|/
    |      /
    |
    +---------
    """, """
    +---------
    |       |
    |       O
    |      \|/
    |      / \\
    |
    +---------
    """]
    print(HANGMAN_STATE[len(current_misses)])
    print("Word/Phrase: " + current_word)
    print("Misses: " + current_misses)


def play_against_human_guesser(dictionary, solution=''):
    """Option to be played against computer."""
    if (solution == ''):
        solution = choice(dictionary)
    solution = solution.lower()
    guess_return = ''
    current_misses = ""
    guess = ['_ ' if i.lower() in "abcdefghijklmnopqurstuvwxyz"
             else i for i in solution]
    display("".join(guess), current_misses)
    while (len(current_misses) < 6):
        letter = input("Guess?- ")
        letter = letter.lower()
        if (len(letter) != 1 or letter not in "abcdefghijklmnopqurstuvwxyz"):
            print("Invalid letter.")
        elif (letter in current_misses):
            print("You have already guessed the letter.")
        elif (letter in solution):
            guess_return = guess_return + letter
            for n in range(len(solution)):
                if (solution.find(letter, n) == n):
                    guess[n] = letter
        else:
            current_misses = current_misses + letter
            guess_return = guess_return + letter
        if("".join(guess) == solution):
            display("".join(guess), current_misses)
            print("")
            print("You Won!!")
            return (solution, guess_return)
            break
        display("".join(guess), current_misses)
        if (len(current_misses) == 6):
            print("You Lose. The solution is '" + solution + "'")
            return (solution, guess_return)


def generate_best_list(viable_dictionary):
    """Generates the best possible letter list for a given solution"""
    best_letter = {}
    for i in viable_dictionary:
        best_letter[i] = list(collections.Counter(i.lower()))

    temp = []
    for i in best_letter.values():
        temp.extend(i)
    count = collections.Counter(temp).most_common()
    count.sort(key=lambda letter: letter[0])
    count.sort(key=lambda number: number[-1], reverse=True)
    letters = [x[0] for x in count if(x[0] != ' ')]
    return (viable_dictionary, letters)


def generate_viable_dictionary(dictionary, letter, miss, position = []):
    viable = []
    if not miss:
        for i in dictionary:
            for n in position:
                if (i.find(letter, n) == n):
                    viable.append(i)
    else:
        for i in dictionary:
            if letter not in i:
                viable.append(i)
    letters = generate_best_list(viable)
    return letters


def play_against_computer_guesser(dictionary, solution='', guesses=''):
    """Option to be played against another person."""
    if (solution == ''):
        solution = choice(dictionary)
    solution = solution.lower()
    current_misses = ""
    if guesses != '':
        guess_provided = 1
    else:
        guess_provided = 0
    guess = [
        '_ ' if i in "abcdefghijklmnopqurstuvwxyz" else i for i in solution]
    display("".join(guess), current_misses)
    i = 0
    dictionary = [i for i in dictionary if len(i) == len(solution)]
    if guess_provided != 1:
        viable, current_guess = generate_best_list(dictionary)

    while (len(current_misses) < 6):
        if guess_provided == 1:
            letter = guesses[i].lower()
        else:
            for i in current_guess:
                if i not in current_misses:
                    if i not in guesses:
                        letter = i
                        break
        if (letter not in "abcdefghijklmnopqurstuvwxyz"):
            print("Invalid letter.")
        elif (letter in current_misses):
            print("You have already guessed the letter.")
        elif (letter in solution):
            position = []
            for n in range(len(solution)):
                if (solution.find(letter, n) == n):
                    guess[n] = letter
                    guesses += letter
                    position.append(n)
            viable, current_guess = generate_viable_dictionary(
                viable, letter, 0,position)
        else:
            current_misses += letter
            viable, current_guess = generate_viable_dictionary(
                viable, letter, 1)
        if("".join(guess) == solution):
            display("".join(guess), current_misses)
            print("")
            print("Computer Wins!!")
            return (solution, guesses)
        display("".join(guess), current_misses)
        if (len(current_misses) == 6):
            print("Computer Loses. The solution is '" + solution + "'")
            return (solution, guesses)
        if(guess_provided == 1):
            if(i < len(guesses) - 1):
                i += 1
            else:
                print(
                    "Maximum guesses reached." +
                    "Restart the game. Computer Loses.")
                break
        if(viable == []):
            print("Word not present in the dictionary!!")
            break


if __name__ == "__main__":
    dictionary = get_dictionary('ospd.txt', type_='file', single_word=False)
    # dictionary = get_dictionary(
    #     'Python is awesome', type_='text', single_word=True)
    # play_against_human_guesser(dictionary, "Python")
    play_against_computer_guesser(dictionary, '', guesses='')
