#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # You can make a block of code execute over and over again using a while statement.
    # The code in a "while" clause will be executed as long as the while statement’s condition is True.

    print('This code laughs at your coding skills.')
    print('How big does this laugh have to be?')
    print('Enter the number.')   # introduction
    laughs = int(input())  # select a number

    while laughs > 0:
        print('Ha')
        laughs = laughs - 1
        # inside the loop we print our laugh and decrease the variable by 1
    # the while loop lasts until the variable becomes 0


# the int() around the input() is needed if we want to use the integer inside the string
# if we write a character instead of an integer we get an error
# if we put a negative number we don't get an error because we still met the "while" statement
# a statement like this works fine but doesn't consider the edge cases, like a negative number.

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.

if __name__ == '__main__':
    main()
