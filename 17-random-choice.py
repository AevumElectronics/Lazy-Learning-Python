#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import random  # import the module for random functionalities.

    vector = ['pizza', 'pasta', 'mozzarella', 'tonno', 'olive', 'olio', 'birra', 'pane']

    print(vector)

    print(random.choice(vector))
    # the random.choice(list) function will return a randomly selected item from the list.
    random.shuffle(vector)
    print(vector)
    # the random.shuffle(list) function will reorder the items in a list.

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
