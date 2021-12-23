#!/usr/bin/python -tt



# Gather our code in a main() function
def main():

    print('Hello Darling!')
    # The function "print" show you the string we write in it

    print('What is your name?')  # ask for their name
    myName = input()
    # myName is a variable we create for storing out input
    # input() is the function that we use to take information from the terminal

    # when we write our name in the terminal, the string gets captured by our function input()
    # and get stored in the variable myName

    print('What is your age?')  # ask for their age
    myAge = input()

    print('It is good to meet you, ' + myName)
    # the function print the string between the '...' plus the myName variable

    print('The length of your name is:')
    print(len(myName))
    # len() show you the length of a string
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    # int() set the variable as an integer
    # if you try to put a string instead of a number you will get an error



# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.
if __name__ == '__main__':
    main()
