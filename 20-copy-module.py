#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import copy  # module for the copy() deepcopy() function

    # we copy our list using the copy() function
    vector = ['pizza', 'pasta', 'mozzarella', 'tonno', 'olive', 'olio', 'birra', 'pane']

    print("Our list is:")
    print(vector)
    print("the ID of the list is: " + str(id(vector)))
    # id(vector) returns the address where the string is stored.

    # copy(list) makes a copy of our list
    # the copy is stored in another memory address
    spesa = copy.copy(vector)

    # now that we have a saved copy we can modify the vector
    vector[1] = 42
    print("Our modified list is:")
    print(vector)

    print("Our copied list is:")
    print(spesa)
    print("the ID of the copied list is: " + str(id(spesa)))
    # id(spesa) returns the address where the copied string is stored.

    # if the list you need to copy contains lists, then use the copy.deepcopy() function
    # instead of copy.copy().


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
