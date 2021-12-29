#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    vector = ['pizza', 'pasta', 'mozzarella', 'tonno', 'olive', 'olio', 'birra', 'pane']

    print(vector)

    print(vector.index('tonno'))
    # list.index(item) returns the index of the list in which the item is stored.
    # if the item is not in the list you will get a ValueError error.

    print("Insert an item on the list:")
    name = input()
    vector.append(name)  # list.append(name) will add a new element at the end of the list.
    print("List with 'append':")
    print(vector)

    # list.remove(name) will remove the first item of the list with that value
    print("The list after the 'remove' is the starting list")
    vector.remove(name)
    print(vector)

    vector.insert(3, name)
    # list.insert(index, name) will add a new element at any index in the list.
    print("List with 'insert':")
    print(vector)

# for easy of understanding we add an element with 'append', then we remove it
# so the resulting list is unchanged, and then we add the same element but with the function 'insert'.

# list.remove(name) will return a ValueError error if we try to remove an item that doesn't exist.

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
