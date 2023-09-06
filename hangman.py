# assignment: programming assignment 1
# author: Grant Bellotti
# date: January 12th, 2023
# file: hangman.py is a program that allows users to play hangman with a computer
# input: The user will input numbers and letters in order to set up and play the game.
# output: The program will output information on the status of the game depending on the user's input.

import random
import os

dictionary_file = "dictionary_short.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    try:
        with open(os.path.dirname(__file__) + "\\" + filename, "r") as f: #read
        #with open(filename, "r") as f: #read
            for i in f.readlines():
                i = i.stri4p().replace("\\n", "")
                if(len(i) > max_size and max_size in dictionary):
                    dictItem = list(dictionary[max_size])
                    dictItem.append(i)
                    dictionary[max_size] = dictItem

                elif len(i) > max_size and max_size not in dictionary:
                    dictionary[max_size] = [i]

                elif (len(i) in dictionary) and (len(i) > 0):
                    dictItem = list(dictionary[len(i)])
                    dictItem.append(i)
                    dictionary[len(i)] = dictItem

                elif len(i) not in dictionary and (len(i) <= max_size) and (len(i) > 0):
                    dictionary[len(i)] = [i]
    except Exception :
        pass

    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options() :
    size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]:\n"))
    if (size < 3) or (size > 12):
        size = random.randint(3,12)
    print(f"The word size is set to {size}.")

    try:
        lives = int(input("Please choose a number of lives [1 - 10, default 5]:\n"))
        if (lives < 1) or (lives > 10):
            lives = 5
    except Exception:
        lives = 5
    print("You have",lives, "lives.")

    return (size, lives)

def interface(splitWord, lives, maxLives, letters):
    lettersChosen  = ', '.join(letters)
    goodLetters = 0
    print("Letters chosen:", lettersChosen)
    printVal = ''
    for i in splitWord:
        if (i in letters) or i == "-":
            printVal += (f'{i}  ')
            goodLetters += 1
        else:
            printVal += ('__  ')
    printVal += f" lives: {lives} "
    for i in reversed(range(maxLives)):
        if i+1 <= lives:
            printVal += 'O'
        else:
            printVal += 'X'
    print(printVal)
    if goodLetters == len(splitWord):
        return True
    return False


def runGame() :
    size, lives = get_game_options()
    maxLives = lives
    numCorrect = 0
    letters = []

    dictSize = dictionary[size]
    word = str(random.choice(dictSize)).upper()
    splitWord = [*word]

    #print(word)
    endGame = False
    
    while (lives > 0 and endGame == False):
        endGame = interface(splitWord, lives, maxLives, letters)
        if endGame == True:
            print(f'Congratulations!!! You won! The word is {word}!')
            break
        userLetter = ''
        while True:
            try:
                userLetter = str(input('Please choose a new letter >\n')).upper()
            except ValueError:
                continue

            if userLetter in letters:
                print("You have already chosen this letter.")
                continue
            elif userLetter.isalpha() == False:
                continue
            elif len(userLetter) > 1:
                continue
            else:
                letters.append(userLetter)
                break
        
        if userLetter in word:
            print('You guessed right!')
            numCorrect += 1

        elif lives == 1:
            print('You guessed wrong, you lost one life.')
            lives -= 1
            interface(splitWord, lives, maxLives, letters)
            print(f'You lost! The word is {word}!')
        else:
            print('You guessed wrong, you lost one life.')
            lives -= 1
        

    playAgain = str(input('Would you like to play again [Y/N]?\n')).upper()
    if playAgain == "Y":
        runGame()
    else:
        print('Goodbye!')

if __name__ == '__main__' :

    dictionary = import_dictionary(dictionary_file)
    #print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary
    print("Welcome to the Hangman Game!")
    runGame()
