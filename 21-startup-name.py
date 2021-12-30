#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import random
    import string

    print("Select the number of letter:")
    num = int(input())  # length of your company name

    for i in range(5):  # modify if you want more than 5 names
        vector = random.choices(string.ascii_uppercase, k=num)
        print('StartUp Name ' + str(i+1) + ': ' + ' '.join(vector))

# random.choices() generate random elements
# the string.ascii_uppercase return an uppercase ascii character as a string
# k=num is the parameter we use to select the length of the list
# the ' '.join(vector) function joins the list as one element

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
