import functions

functions.welcome()
first_time = True
    
while True:
    try:
        if first_time:
            action = '0'
            first_time = False
        else:
            action = functions.get_action()
        if action == '0':
            text = functions.get_text()
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
            functions.replace_word(text, old_word, new_word)  
        elif action == '4':
            print("FIXME: Add encoding function.")
        elif action == '5':
            print("FIXME: Add special feature.")
        else:
            raise functions.QuitError
    except functions.QuitError:
        break

print('\nHave a nice day!')
