#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # Lists are used to store multiple items in a single variable.
    # Vector=[Vector[0],Vector[1],Vector[2],Vector[3],Vector[4]]

    vector = ['cat', 'dog', 'bau', 'miao', 42, 69, 420, 0.01, True, False]
    # we can put anything inside our list: 'strings', numbers, Booleans
    print('Our base vector is this:')
    print(vector)
    # the vector has 10 elements so the index goes from 0 to 9
    print('Pick a number between 0 and 9')
    num = int(input())  # the index must be an integer
    print('the index number '+str(num) + ' points at the item:')
    print(vector[num])  # vector[x] is the item stored in the x position of our list


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
