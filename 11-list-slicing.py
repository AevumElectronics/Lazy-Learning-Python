#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # Lists are used to store multiple items in a single variable.
    # Vector=[Vector[0],Vector[1],Vector[2],Vector[3],Vector[4]]
    # List slicing is used to access a range of elements in a list
    # Vector[ Initial : End : IndexJump ]

    vector = ['cat', 'dog', 'bau', 'miao', 42, 69, 420, 0.01, True, False]
    print('Our base vector is this:')
    print(vector[:])  # vector[:] without indexes displays the full list

    # if we want to slice only the end or the beginning of a list
    print('Choose the starting point of the vector (between 0 and 9)')
    start = int(input())
    print('Your sliced list is:')
    print(vector[start:])  # the "start" index is included
    print('Choose the ending point of the vector(between 0 and 9)')
    end = int(input())
    print('Your sliced list is:')
    print(vector[:end])  # the "end" index is NOT included


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
