#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    # a dictionary is a mutable collection of many values.
    # dictionary = {key: key-value, key2: key-value2}

    birthdays = {'Bob': 'Apr 5', 'robert': 'Dec 22', 'Alice': 'Mar 14'}
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break  # if the input is a blank we break the loop

        if name in birthdays:  # if the name is in the dictionary we enter the condition.
            print(birthdays[name] + ' is the birthday of ' + name)

        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday  # name is the key and bday is key-value.
            print('Birthday database updated.')

    print("All our dictionary keys:")
    for i in birthdays.keys():
        print(i)    # the variable "i" is used to extract the keys.

    print("All our dictionary values:")
    for i in birthdays.values():
        print(i)    # the variable "i" is used to extract the key-values.

    print("The dictionary (key: key-value):")
    for i in birthdays.items():
        print(i)    # the variable "i" is used to extract both the keys and the key-values.


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
