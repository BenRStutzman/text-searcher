# Remove reloading feature when finished.
import os
from imp import reload
import functions

mod_time = os.path.getmtime(functions.__file__)

functions.welcome()
first_time = True
    
while True:
    try:
        if first_time:
            action = '0'
            first_time = False
        else:
            action = functions.get_action()
            new_mod_time = os.path.getmtime(functions.__file__)
            if new_mod_time > mod_time:
                reload(functions)
                mod_time = new_mod_time
                print('Reloaded functions module')
        if action == '0':
            text, filename = functions.get_text()
        elif action == '1':
            word = functions.get_word("Please enter a word or phrase to "
                                              "find in the text: ")
            functions.print_frequency(text, word)
        elif action == '2':
            word = functions.get_word("Please enter a word or phrase to "
                                              "find in the text: ")
            functions.print_instances(text, word)
        elif action == '3':
            old_word = functions.get_word("Please enter a word or phrase to "
                                                  "find in the text: ")
            new_word = functions.get_word("Please enter a word or phrase to "
                                          "replace '%s': " % old_word.lower())
            functions.replace_word(text, filename, old_word, new_word)
        elif action == '4':
            shift = functions.get_shift()
            functions.caesar_shift(text, filename, shift)
        elif action == '5':
            functions.print_frequency_list(text)
        else:
            raise functions.QuitError
    except functions.QuitError:
        break

print('\nHave a nice day!')
