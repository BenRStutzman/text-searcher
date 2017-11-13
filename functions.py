""" Contains the functions for 'Text_searcher.py' """

import time
import smtplib
import os
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from imp import reload

class QuitError(Exception):
    """ Error that will be raised when the user enters 'q'. """
    pass

def welcome():
    """ Welcome the user and give instructions. """
    print("Hello there!")
    time.sleep(1)
    print("Please follow the instructions to "
          "have fun with a text file of your choice.")
    time.sleep(2)
    print("At any time, you may enter 'q' to quit.")
    time.sleep(2)
    print("Let's begin!")
    time.sleep(1)
    print('')

def get_text():
    """ Open the text file entered by the user, and prompt again
    if the file doesn't exist. """
    filename = input('Please enter the name of a text file, '
                     'including the extension: ')
    while True:
        if filename.lower() == 'q':
            raise QuitError
        try:
            with open(filename, 'r+') as f:
                text = f.read()
                print("Upload successful!")
                time.sleep(1)
                return (text, filename)
        except FileNotFoundError:
                filename = input("Sorry, that file wasn't found. Enter "
                                "another file name: ")

def get_action():
    """ Give the user a menu of choices, and return his/her selection. """
    action = input("\nWhat would you like to do?\n"
                   "(0) Choose a new text\n"
                   "(1) Find the number of times a word or phrase appears\n"
                   "(2) Find all instances of a word or phrase\n"
                   "(3) Replace a word or phrase with another word or phrase\n"
                   "(4) Encode the text with a Caesar cipher\n"
                   "(5) Print frequency list\n"
                   "(6) Email myself text with a keyword\n"
                   "(7) Email myself a random chunk of text\n"
                   "\nEnter the number corresponding to your choice: ")
    while True:
        if action.lower() == 'q':
            raise QuitError
        elif action in list('01234567'):
            return action
        else:
            action = input("Sorry, that's not a valid choice. Please "
                           "enter an integer, 0 through 7: ")

def get_word(prompt):
    """ Ask the user for a word with a given prompt, and return that word. """
    while True:
        word = input(prompt)
        if word.lower() == 'q':
            raise QuitError
        elif word:
            return word
        else:
            print("Sorry, make sure to enter a word or phrase.")


def get_chunk(text, location, radius):
    """ Return the first chunk of text with a user-specified keyword. """
    if radius <= location <= len(text) - radius:
        chunk = text[location - radius:location + radius]
    elif location <= radius <= len(text) - radius:
        chunk = text[:location + radius]
    elif radius <= len(text) - radius <= location:
        chunk = text[location - radius:]
    else:
        chunk = text
    return '...' + chunk + '...'

def print_frequency(text, word):
    """ Print the number of times a string appears in a piece of text. """
    print("Searching text...")
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
    """ Print all instances of a word or phrase in the text, plus some text
    around it, and allow user to cycle through or return to the main menu. """
    print("Searching text...")
    location = text.lower().find(word.lower())
    if location == -1:
        print("Sorry, '%s' doesn't appear in the text." % word.lower())
        time.sleep(1)
        return
    frequency = text.lower().count(word.lower())
    if frequency == 1:
        plural = ''
    else:
        plural = 's'
    print("'%s' appears %d time%s.\nPress enter to continue to the "
          "next instance, or enter 'm' to return "
          "to the main menu." % (word.lower(), frequency, plural))
    time.sleep(2)
    instance = 1
    onward = ''
    while instance <= frequency:
        if onward == 'q':
            raise QuitError
        elif onward == '':
            print('\n%d) %s' % (instance, get_chunk(text, location, 50)))
            location = text[location + 1:].lower().find(
                       word.lower()) + location + 1
            onward = input()
            instance += 1
        else:
            return
    if onward == '':
        print("That's all!")
        time.sleep(1)

def replace_word(text, filename, old_word, new_word):
    """ Replace all instances of a word or phrase with another word or phrase,
    then save the replaced text in a new file. """
    if old_word.lower() not in text.lower():
        print("Sorry, '%s' doesn't appear in the text." % old_word.lower())
        time.sleep(1)
        return
    print("Searching and replacing...")
    new_name = filename.replace('.txt', '_r.txt')
    with open(new_name, 'w+') as f:
        f.write(text.replace(old_word.title(), old_word.lower()).replace(
                old_word.lower(), new_word))
    print("Replacement successful! Your new text is in "
          "the file '%s'." % new_name)
    time.sleep(1)

def get_shift():
    """ Ask the user for a Caesar shift value to encode the text. """
    shift = input("Please enter a Caesar shift value (1 - 25): ")
    while True:
        if shift.lower() == 'q':
            raise QuitError
        try:
            return int(shift) % 26
        except ValueError:
            shift= input("Sorry, that's not a valid shift. Please enter "
                         "an integer, 1 through 25: ")

def caesar_shift(text, filename, shift):
    """ Shift all letters in the text by a specified value, then save the
    encoded text in a new file. """
    print("Encoding text...")
    shifted = ''
    for letter in text:
        if letter.isalpha():
            if letter <= 'Z':
                letter = chr(ord(letter) + shift)
                if letter > 'Z':
                    letter = chr(ord(letter) - 26)
            else:
                letter = chr(ord(letter) + shift)
                if letter > 'z':
                    letter = chr(ord(letter) - 26)
        shifted += letter
    new_name = filename.replace('.txt', '_e.txt')
    with open(new_name, 'w+') as f:
        f.write(shifted)
    print("Encoding successful! Your new text is in "
          "the file '%s'." % new_name)
    time.sleep(2)

def print_frequency_list(text):
    """ Print a list of all words in the text, from most to least frequent. """
    print("Creating frequency list...")
    words = {}
    text = text.lower().replace('/', ' ').replace('-', ' ').replace('—', ' ')
    for word in text.split():
        word = str.strip(word, string.punctuation + "0123456789’“”")
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    ordered = []
    for item in words.items():
        ordered.append(item)
    ordered.sort(key = lambda item: item[1], reverse = True)
    ordered = [item[0] for item in ordered]
    if '' in ordered:
        ordered.remove('')
    print("\nHere are all %d words in the text, from most to least frequent:\n"
          % len(ordered))
    time.sleep(2)
    for word in ordered:
        plural = ''
        if words[word] > 1:
            plural += 's'
        print("%5d) '%s' appears %d time%s." % (ordered.index(word) + 1,
                                          word, words[word], plural))
    time.sleep(1)

def get_location(text, word):
    """ Find the index of the first instance of a word in the text. """
    print("Searching text...")
    location = text.lower().find(word.lower())
    if location == -1:
        print("Sorry, '%s' doesn't appear in the text." % word.lower())
        time.sleep(1)
    return location

def verify_email(chunk, header):
    """ Ask the user if they would like a printed chunk emailed to them. """
    print('\n%s' % header)
    time.sleep(2)
    choice = input("\n%s\n\nOK to send email with the above "
                   "chunk of text? (Enter 'yes' or 'no'): " % chunk)
    if choice.lower() == 'q':
        raise QuitError
    elif choice.lower() == 'yes':
        return True
    else:
        print("Very well, you will not receive an email.")
        time.sleep(1)
        return False

def email_chunk(filename, chunk, address):
    """ Email a chunk of text to the user. """
    print("Sending message...")
    try:
        my_address = 'ben.stutzman.unofficial@gmail.com'
        message = MIMEMultipart()
        message['From'] = my_address
        message['To'] = address
        message['Subject'] = 'Text chunk from ' + filename
        body = chunk
        message.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
        server.starttls()
        server.login(my_address, 'Boa8Constrictor9')
        message = message.as_string()
        server.sendmail(my_address, address, message)
        server.quit()
        print("Message sent!")
    except smtplib.SMTPRecipientsRefused:
        print("Sorry, email address is invalid.")
    time.sleep(1)

def update_functions(module, mod_time):
    """ Reload a module if it has been modified since the last check. """
    new_mod_time = os.path.getmtime(module.__file__)
    if new_mod_time > mod_time:
        reload(module)
        print('---Reloaded functions module---')
    return new_mod_time
    
if __name__ == '__main__':
    print("This file contians the functions for 'Text_searcher.py'.")
