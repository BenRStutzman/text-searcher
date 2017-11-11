""" Contains the functions for 'Text_searcher.py' """

import time

def welcome():
    """ Welcome the user and give instructions. """
    print("Hello there!")
    time.sleep(0)
    print("Please follow the instructions to "
          "have fun with an inspirational text.")
    time.sleep(0)
    print("At any time, you may enter 'q' to quit.")
    time.sleep(0)
    print("Let's begin!\n")
    time.sleep(0)

def get_text():
    """ Open the text file entered by the user, and prompt again
    if the file doesn't exist. """
    filename = input('Please enter the name of a text file, '
                     'including the extension: ')
    while True:
        try:
            with open(filename, 'r+') as f:
                text = f.read()
                print("\nYour text has been imported.")
                return ('0', text)
        except FileNotFoundError:
            if filename == 'q':
                    return ('q', '')
            else:
                filename = input("Sorry, that file wasn't found. Enter "
                                "another file name: ")

def get_action():
    """ Give the user a menu of choices, and return his/her selection. """
    while True:
        action = input("\nWhat would you like to do?\n"
                            "(0) Choose a new text\n"
                            "(1) Find the number of times a word or phrase "
                            "appears\n"
                            "(2) Find all instances of a word or phrase\n"
                            "(3) Replace a word or phrase with another word or phrase\n"
                            "(4) Encode the text with a Caesar cipher\n"
                            "(5) Suprise me\n"
                            "Enter the number corresponding to your choice: ")
        if action in list('012345q'):
            return action
        else:
            print("Sorry, that's not a valid choice.")

def get_word():
    """ Ask the user for a word or phrase to search for. """
    while True:
        word = input("\nPlease enter a word or phrase to search for: ")
        if word == 'q':
            return ('q', '')
        elif word:
            return ('0', word.lower())
        else:
            print("Sorry, make sure to enter a word or phrase.")

def print_frequency(text, word):
    frequency = text.count(word)
    if frequency == 1:
            plural = ''
    else:
        plural = 's'
    print("'%s' appears %d time%s." %(word, frequency, plural))



if __name__ == '__main__':
    print("This file contians the functions for 'Text_searcher.py'.")
            
