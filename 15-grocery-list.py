#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # The grocery list:
    # The "in"/"in not" operators scans the list to determine whether a value is or isn’t in a list.
    # The result is a Boolean. (True or False)
    vector = ['pizza', 'pasta', 'mozzarella', 'tonno', 'olive', 'olio', 'birra', 'pane']

    while True:
        # This list will add a missing element and will remove an already present element.
        print("Our grocery list is:")
        print(vector)

        print("Enter an item name")
        name = input()
        if name in vector:  # the statement is true only if the element is on the list
            print("The " + str(name) + " is already on the list")
            print("The element will be removed from the list")
            index = vector.index(name)
            # list.index() returns the first index position of a specified element in the List.
            del vector[index]   # the "del" statement will delete values in a list.

        elif name not in vector:    # the statement is true only if the element is NOT on the list
            print("The " + str(name) + " is not on the list")
            print("The element will be added on the list")
            vector = vector + [name]  # list concatenation


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
