#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import sys
    import pyinputplus as pyip  # input validation
    # install the module with: pip install pyinputplus

    # validate a number
    print("how old are you?")
    age = pyip.inputNum()
    print("what's your name?")
    # validate a string
    name = pyip.inputStr()

    print("you are " + str(age) + " old.")
    print("your name is: " + str(name) + ".")



'''
inputStr() Is like the built-in input() function but has the general PyInputPlus features.
inputNum() Ensures the user enters a number and returns an int or float
inputChoice() Ensures the user enters one of the provided choices
inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options
inputDatetime() Ensures the user enters a date and time
inputYesNo() Ensures the user enters a “yes” or “no” response
inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value
inputEmail() Ensures the user enters a valid email address
inputFilepath() Ensures the user enters a valid file path and filename
inputPassword() Is like the built-in input(), but displays * characters as 
the user types so that passwords, or other sensitive information, aren’t 
displayed on the screen
'''

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
