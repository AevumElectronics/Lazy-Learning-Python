#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import random   # import the module for calling random numbers
    import sys      # import the module sys, that provides various functions and variables

    while True:
        print("Guess what number I'm thinking of")
        print('Type a number between 0 and 5.')
        number = int(input())
        response = random.randint(0, 5)  # the function calls a random integer number between a range
        if number == response:
            print('You got it!')
            sys.exit()  # the call sys.exit() terminate the program
        print('Your number was ' + str(number) + ' while mine was ' + str(response))
        print('Try again!')

# the "while" loop goes on forever until we terminate the program with the sys.exit() call
# when you print the numbers you want to print the string while in the "if" you will need the integers.

# int(variable) is the integer | str(variable) is the string

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
