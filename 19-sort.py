#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    # sort() is used to sort elements on the list.
    # sort() uses “ASCIIbetical order” rather than actual alphabetical.
    # if you have a string the uppercase came first : Z will be sorted before a

    vector = ['pizza', 'pasta', 'mozzarella', 'tonno', 'olive', 'olio', 'birra', 'pane']

    print("Our initial list is:")
    print(vector)
    vector.sort()  # the initial list is all lowercase so list.sort() will be alphabetical
    print("Our sorted list is:")
    print(vector)

    # if we want to order the values in reverse order (anti-alphabetical)
    vector.sort(reverse=True)
    print("Our reversed alphabetical list is:")
    print(vector)

    # we change the list to add some uppercase letter
    vector = ['pizza', 'Pasta', 'mozzarella', 'tonno', 'Olive', 'olio', 'birra', 'pane']
    print("The sorted list with uppercase letters is:")
    vector.sort()
    print(vector)

    # if we want to reverse the order of the items in a list
    vector.reverse()
    print("Our reversed order list is:")
    print(vector)

    # if we want to tread uppercase like lowercase "key=str.lower" will help us
    vector.sort(key=str.lower)
    print("Sorted list:")
    print(vector)

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
