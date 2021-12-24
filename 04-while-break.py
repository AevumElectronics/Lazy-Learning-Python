#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # You can make a block of code execute over and over again using a while statement.
    # The code in a "while" clause will be executed as long as the while statement’s condition is True.
    # A "break" statement immediately exits the "while" loop’s clause.

    print('This code want you to yell.')  # introduction
    print("What's your name darling?")
    name = input()  # insert your name
    while True:
        if name.upper() == name:  # name.upper() returns a string where all characters are in upper-case.
            break                 # if our name is written in upper-case the "if" condition is true

        print('WHAT?')  # you need to yell your name.
        name = input()  # we change the name, so we have a chance of getting out of the loop.

    print('Oh!...hi ' + name.lower())
# name.lower() returns a string where all characters are in lower-case.


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.

if __name__ == '__main__':
    main()
