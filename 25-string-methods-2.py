#!/usr/bin/python -tt

# Gather our code in a main() function
def main():

    # partition() returns a tuple of three substrings for the “before,” “separator,” and “after”
    vector = "This is what happens when you try to use partition():"
    print(vector)
    print(vector.partition('try'))  # in this case 'try' is the separator

    # let's save the partition and do something funky
    print("Let's justify the text:")
    newvec = vector.partition('try')
    print(newvec[0].ljust(80))  # left justify in a string of total length 80.
    print(newvec[1].center(80, '-').swapcase())
    print(newvec[2].rjust(80))  # right justify in a string of total length 80.
    # newvec is a tuple made by 3 strings, we print every element in a different way.
    # center(80, '-')  centers the text in a string long 80 where instead of using spaces we use '-'
    # swapcase() is used to swap uppercase to lowercase and vice versa.


# similar functions are made to remove the spaces
# strip()
# rstrip()
# lstrip()


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
