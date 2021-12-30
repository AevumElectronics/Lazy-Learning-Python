#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import pprint   # the “pretty print” shows a cleaner display of dictionary’s values.
    animals = {'name': 'Pooka', 'age': 5}

    # the setdefault() method is a nice shortcut to ensure that a key exists
    animals.setdefault('color', 'black')
    # animals become {'color': 'black', 'age': 5, 'name': 'Pooka'}
    # the setdefault is done once, another setdefault is useless as the "color" key now exist.

    print("Our Dictionary:")
    print(animals)
    print("Our Pretty Printed Dictionary:")
    pprint.pprint(animals)
    # print(pprint.pformat(animals)) is an alternative way

    # get() method that takes two arguments: the key of the value to retrieve
    # and a value to return if that key does not exist.
    print("the age is present on the dictionary so the value is:")
    print(animals.get('age', 0))
    print("the number of puppies is NOT present on the dictionary so the value is:")
    print(animals.get('puppies', 0))


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
