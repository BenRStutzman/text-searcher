import functions

functions.welcome()

action, text = functions.get_text()
    
while action != 'q':
    action = functions.get_action()
    if action == '0':
        action, text = functions.get_text()
        if action == 'q':
            break
    elif action == '1':
        action, word = functions.get_word()
        if action == 'q':
            break
        else:
            functions.print_frequency(text, word)
        
    else:
        break

print('Have a nice day!')
