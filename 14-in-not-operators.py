#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # We want to check the grocery list:
    # The "in"/"in not" operators scans the list to determine whether a value is or isn’t in a list.
    # The result is a Boolean. (True or False)
    vector = ['pizza', 'pasta', 'mozzarella', 'tonno', 'olive', 'olio', 'birra', 'pane']

    print("Our grocery list is:")
    print(vector)
    print("Enter an item name and see if is on the list")
    name = input()
    if name in vector:  # the statement is true only if the element is on the list
        print("The " + str(name) + " is already on the list")
    elif name not in vector:    # the statement is true only if the element is NOT on the list
        print("The " + str(name) + " is not on the list")


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
