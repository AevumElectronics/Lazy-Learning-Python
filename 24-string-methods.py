#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    """
    we can write a comment as a multiple string using 3 apostrophe.
    we avoid using \'  \"  \t for the tab  \n for the line break and \\ for the backslash
    print(r'string') print a raw string
    """

    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')
    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')


# upper()    uppercase
# lower()    lowercase
# isupper()  Will return a Boolean True value
# islower()  Will return a Boolean True value
# isalpha()  Returns True if the string consists only of letters and isn’t blank
# isalnum()  Returns True if the string consists only of letters and numbers and is not blank
# isdecimal()  Returns True if the string consists only of numeric characters and is not blank
# isspace()  Returns True if the string consists only of spaces, tabs, and newlines and is not blank
# istitle()  Returns True if the string begin with an uppercase letter followed by only lowercase letters
# startswith()  Return True if the string value they are called on, begins with the string
# endswith()  Return True if the string value they are called on, ends with the string
# join()   Transform a list of strings that need to be joined together into a single string value
# split()  Transform a string value into a list of strings.


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
