   ###########################################################
    #  Computer Project #4
    #
    # Main Function
    #  Display opening message
    #  call 2 functions (Get character, Find state)
    #   call Function 1 (Get character)  
    #      input a character that meets correct length
    #   call Function 2 (Find state)
    #       determine state based on character
    #   loop while character is not empty string
    #    display message if whether user is or is not laughing
    ###########################################################


def get_ch():
    """
    Takes a character as input and tries again if the input is invalid
    """
    user_input = input('Enter a character or press the Return key to finish: ')
    if len(user_input) > 1:
        print ('Invalid input, please try again.')
        return 'invalid'

    else:
        return user_input


def find_state(state, ch):
    
    """
    Determines and assigns state of character based on character entered and
    state = 5 if chracter is invalid.
    """
        # state 5 is an invalid entry
    
    if state == '1':
        if ch == 'h':
            state = '2'
        else:
            state = '5'
            
            
    elif state == '2':
        if ch == 'a' or ch == 'o':
            state = '3'
        else:
            state = '5'
            
            
    elif state == '3':
        if ch == '!':
            state = '4'
            
        elif ch == 'h':
            state = '2'
            
        elif ch == 'a' or ch == 'o':
            state = '3'
            
        else:
            state = '5'
            
    elif state == '4':
        if ch != '':
            state = '5'
        else:
            state = '4'
        
  
    return state
  

def main():
    """
    Calls get_ch function and find_state function. Loops while character is
    not invalid. Displays whether user is or is not laughing based on state.
    """
    state = '1'
        #user will always begin with state 1
    final_ch = ''
       #final_ch begins with empty string to keep track of characters 
    ch = 'a'
    print ('I can recognize if you are laughing or not.')
    print('Please enter one character at a time.\n')
        # Opening message 
    while ch != '':    
        ch = get_ch()
        if ch != 'invalid':
            state = find_state(state, ch)
            ch = str(ch)
            final_ch += ch
        #loop while character does not equal empty string
        
        
    if state == '4':
        print(  "You entered ", final_ch)
        print('You are laughing.')
           
    if state == '5':
        print ("You entered ", final_ch)
        print('You are not laughing.')

main()