#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # Lists are used to store multiple items in a single variable.
    # Vector=[Vector[0],Vector[1],Vector[2],Vector[3],Vector[4]]
    # List slicing is used to access a range of elements in a list
    # Vector[ Initial : End : IndexJump ]
    # the "start" index is included
    # the "end" index is NOT included

    vector = ['cat', 'dog', 'bau', 'miao', 42, 69, 420, 0.01, True, False]

    # IndexJump is used when we want to jump in the list
    # the vector is not [:] anymore but [::n] where n is the index jump
    print('Our full list is:')
    print(vector[::])  # we show every element of the list one after the other
    print('IndexJump is 2: One element is shown, one element is jumped.')
    print(vector[::2])
    print('IndexJump is 3: One element is shown, two elements are jumped.')
    print(vector[::3])

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
