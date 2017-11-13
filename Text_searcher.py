""" Allows the user to import a text file and use various features to
search for words, encode the text, and send portions by email. """

import functions
import random

# Checks when the functions module was last saved, for future reloading
mod_time = functions.os.path.getmtime(functions.__file__)

functions.welcome()
first_time = True

# Loops until the user decides to quit
while True:
    try:
        if first_time:
            action = '0'
            first_time = False
        else:
            # Gives the user a menu of actions to choose from
            action = functions.get_action()
            # Reloads the functions file if it's been updated
            mod_time = functions.update_functions(functions, mod_time)
        # Executes the appropriate feature depending on the action choice
        if action == '0':
            # Lets the user choose a new text file
            text, filename = functions.get_text()
        elif action == '1':
            # Counts how many times a word or phrase appears
            word = functions.get_word("Please enter a word or phrase to "
                                              "find in the text: ")
            functions.print_frequency(text, word)
        elif action == '2':
            # Prints all instances of a word or phrase
            word = functions.get_word("Please enter a word or phrase to "
                                              "find in the text: ")
            functions.print_instances(text, word)
        elif action == '3':
            # Replaces a word or phrase with another word or phrase
            old_word = functions.get_word("Please enter a word or phrase to "
                                                  "find in the text: ")
            new_word = functions.get_word("Please enter a word or phrase to "
                                          "replace '%s': " % old_word.lower())
            functions.replace_word(text, filename, old_word, new_word)
        elif action == '4':
            # Caesar-shifts all letters in the text by a desired amount
            shift = functions.get_shift()
            functions.caesar_shift(text, filename, shift)
        elif action == '5':
            # Prints a list of all words in the text by frequency
            functions.print_frequency_list(text)
        elif action == '6':
            # Emails the user a chunk of text with a keyword
            word = functions.get_word("Please enter a keyword or phrase: ")
            location = functions.get_location(text, word)
            if location >= 0:
                chunk = functions.get_chunk(text, location, 500)
                if functions.verify_email(chunk, "Here's the first chunk "
                                          "containing '" + word + "' in " +
                                          filename + ":"):
                    address = functions.get_word("Please enter your email "
                                                 "address: ")
                    functions.email_chunk(filename, chunk, address)
        else:
            # Emails the user a random chunk of text
            location = random.randint(0, len(text) - 1)
            chunk = functions.get_chunk(text, location, 500)
            if functions.verify_email(chunk, "Here's a random chunk "
                                      "from " + filename + ":"):
                address = functions.get_word("Please enter your email address: ")
                functions.email_chunk(filename, chunk, address)
    except functions.QuitError:
        # Exits the loop if the user ever enters 'q'
        break

print('\nHave a nice day!')
