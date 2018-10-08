# python-project

This project represents a finite state machine and will be able to tell whether a user is laughing or not. It can recognize simple patterns of strings such as: ha! haha! hahaha! ho! hoho! hohoho! hahohoho! hahohahoha! Basically, the pattern to be recognized is a sequence of “ha” or “ho”, or a mixture of both. The sequence can be of any length (at least greater than three, i.e., the shortest sequence is “ha!” or “ho!”). There is no restriction on how many “ha”s or “ho”s the sequence can contain, and the “ha”s and “ho”s can appear in any order if the sequence is a mixture of both. The string must end with one “!”. 

The FSM that recognizes those exact string patterns can be drawn as follows: This FSM has 5 states and 9 transitions. State 1 is the start state and state 4 is the successful end state while state 5 is the unsuccessful end state. The transitions indicate how one transits from one state to another. 

Input will come from the user one character at a time (in the get_ch() function). If the input has two or more characters, it prints an error message and prompts for another input. 4. Pressing only the Return key (Enter key) means the user input is finished. 
