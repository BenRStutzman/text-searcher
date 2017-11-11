""" Contains the functions for 'Text_searcher.py' """

import time

class QuitError(Exception):
    pass

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
        if filename == 'q':
            raise QuitError
        try:
            with open(filename, 'r+') as f:
                text = f.read()
                print("Your text has been imported.")
                time.sleep(1)
                return text
        except FileNotFoundError:
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
                            "(5) Surprise me\n"
                            "\nEnter the number corresponding to your choice: ")
        if action in list('012345q'):
            return action
        else:
            print("Sorry, that's not a valid choice.")

def get_word(prompt):
    """ Ask the user for a word with a given prompt, and return that word. """
    while True:
        word = input(prompt)
        if word == 'q':
            raise QuitError
        elif word:
            return word
        else:
            print("Sorry, make sure to enter a word or phrase.")

def print_frequency(text, word):
    """ Print the number of times a string appears in a piece of text. """
    frequency = text.lower().count(word.lower())
    if frequency == 1:
            plural = ''
    else:
        plural = 's'
    if frequency == 0:
        print("Sorry, '%s' doesn't appear in the text." % word.lower())
    else:
        print("'%s' appears %d time%s." %(word.lower(), frequency, plural))
    time.sleep(1)

def print_instances(text, word):
    """ Print all instances of a word or phrase in the text,
    plus some text around it. """
    location = text.lower().find(word.lower())
    if location == -1:
        print("Sorry, '%s' doesn't appear in the text." % word.lower())
        time.sleep(1)
        return
    else:
        print("Here are all %d places '%s' appears:"
              % (text.lower().count(word.lower()), word.lower()))
    time.sleep(1)
    old_location = -1
    instance = 0
    radius = 50
    while location > old_location:
        instance += 1
        if radius <= location <= len(text) - radius:
            print('\n%d) ...%s...' % (instance, text[location - radius:location + 50]))
        elif location <= radius <= len(text) - radius:
            print('\n%d) ...%s...' % (instance, text[:location + radius]))
        elif radius <= len(text) - radius <= location:
            print('\n%d) ...%s...' % (instance, text[location - radius:]))
        else:
            print('\n%d) ...%s...' % (instance, text))
        old_location = location
        location = text[location + 1:].lower().find(word.lower()) + location + 1
    time.sleep(1)

def replace_word(text, old_word, new_word):
    """ Replace all instances of a word or phrase with another word or phrase,
    then save the new text in a file. """
    if old_word.lower() not in text.lower():
        print("Sorry, '%s' doesn't appear in the text." % old_word.lower())
        time.sleep(1)
        return
    with open('text_replaced.txt', 'w+') as f:
        f.write(text.replace(old_word, old_word.lower())
                .replace(old_word.lower(), new_word))
    print("Your new text is in the file 'text_replaced.txt'.")
    time.sleep(1)

if __name__ == '__main__':
    print("This file contians the functions for 'Text_searcher.py'.")
            
