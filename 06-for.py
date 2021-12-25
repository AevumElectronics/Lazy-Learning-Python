#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # if you want to execute a block of code only a certain number of times use the "for" cycle
    # the function range(n) create a sequence of numbers from 0 to (n)

    print("Let's Multiply for 3")
    for i in range(5):
        print(str(i) + ' Times 3= ' + str(3*i))

# inside the "for" loop it's useless to modify the variable "i" because it gets overwritten
# with the next index in the range().

# the index must be printed as a string str(i).

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()

