#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    # our username = 'Aevum'
    # our password = 'Electronics'
    # we want this username & password as the correct one

    print('Hello Darling!')
    print('What is your name?')  # ask for their name
    name = input()  # insert your name into the variable "name"

    # if(statement):
    # if the statement we do is right we enter inside the "if" loop.
    # if the statement we do is false we jump over the loop and continue with the program.
    # if the statement we do is false and there is an "else" condition we jump there.

    if name == 'Aevum':
        # we go into the loop only if the name is right
        print('Hello, Aevum')
        print('Insert the Password')
        password = input()
        if password == 'Electronics':
            # we go into the loop only if the password is right
            print('Access granted.')
        else:
            # we go into the "else" loop if the password is wrong
            print('Wrong password.')
    else:
        print("I Don't know you, go Away!")
        # we get into this "else" condition if the name is wrong.

# remember that strings are case-sensitive.


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
