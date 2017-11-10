import functions

print('Hello there!')

user_choice = 'new'

while user_choice == 'new':
    text = functions.get_text()
    if text == 'q':
        break
    user_choice == ''
    while user_choice == '':
        user_choice = get_action()
        if user_choice == 'q':
            break
        user_choice = input("Press enter to try more actions on this text, "
                            "or enter 'new' to choose a different text ('q' to quit): ")

print('Have a nice day!')
