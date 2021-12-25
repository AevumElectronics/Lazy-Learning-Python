#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # You can make a block of code execute over and over again using a while statement.
    # The code in a "while" clause will be executed as long as the while statement’s condition is True.
    # A "break" statement immediately exits the "while" loop’s clause.
    # A "continue" statement immediately restart the loop

    while True:
        print('Do you want to exit the loop?')
        answer = input()
        if answer != 'yes':
            continue
        print('What do we say?')
        gentile = input()
        if gentile == 'please':
            break
    print('Ok...Now you are out of the loop, bye!')

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()

