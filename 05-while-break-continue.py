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
        if answer != 'yes':  # if your answer is not "yes" you will enter the "if" statement
            continue         # the "continue" statement immediately restart the loop
        print('What do we say?')    # be gentle
        gentile = input()
        if gentile == 'please':
            break   # if you want to exit the "while" loop you will need to say please
    print('Ok...Now you are out of the loop, bye!')

# instead of waiting for the loop to finish, we use the "continue" statement to halve the code inside the loop
# is useless to do stuff if the condition aren't met, so is better to restart.
# the "while" loop goes on forever, the "break" is reachable only if we met all the conditions,
# and it's the only way of getting out of the loop.

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()

