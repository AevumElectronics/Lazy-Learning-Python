#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # enumerate() is a function that return two loop variables:
    # The count of the current iteration.
    # The value of the item at the current iteration.

    # when using a loop we go from 0 to len(list).
    # instead of creating an index and searching for the length of the list we use enumerate().

    vector = ['pizza', 'pasta', 'mozzarella', 'tonno', 'olive', 'olio', 'birra', 'pane']

    print("Our grocery list is:")
    for index, item in enumerate(vector):
        print('The item ' + str(index) + ' in our list is: ' + item)

    # the 'enumerate(list)' returns the index and the item

    print("Our list is:")
    print(vector)  # the base list
    print("The enumerate list is:")
    print(list(enumerate(vector)))
    # the 'list()' constructor returns a list consisting of iterable's items.
    # the 'enumerate' list has both the index and the value stored for every position

    # we can change the starting point of the indexes by using the
    print("The enumerate list starting from 5 is:")
    print(list(enumerate(vector, start=5)))

    # enumerate(list, start=x) use "x" as a start value.

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
