""" Contains the functions for 'Text_searcher.py' """


def get_text():
    """ Open the text file entered by the user, and prompt again
    if the file doesn't exist. """
    filename = input('Please enter the name of a text file, '
                     'including the extension: ')
    while True:
        if filename == 'q':
            return 'q'
        try:
            with open(filename, 'r+') as f:
                return f.read()
        except FileNotFoundError:
            filename = input("Sorry, that file wasn't found. Enter "
                            "another file name, or 'q' to quit: ")

def get_action():
    """ Give the user a menu of choices, and return his/her selection. """
    while True:
        user_choice = ("What would you like to do with this text?\n"
                       "(1) Find the number of times a word or phrase appears\n"
                       "(2) Find all instances of a word or phrase\n"
                       "(3) Search and replace a word or phrase with another word or phrase\n"
                       "(4) Encode the text with a Caesar cipher\n"
                       "(5) Suprise me\n"
                       "'q' Quit\n"
                       "Enter the number corresponding to your choice: ")
        if user_choice in list('12345q'):
            return user_choice
        else:
            print("Sorry, that's not a valid choice.")
        



if __name__ == '__main__':
    print("This file contians the functions for 'Text_searcher.py'.")
            
