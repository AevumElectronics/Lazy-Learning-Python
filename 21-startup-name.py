#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import random
    import string

    print("Select the number of letter:")
    num = int(input())


    for i in range(5):
        vector = random.choices(string.ascii_uppercase, k=num)
        print('StartUp Name ' + str(i+1) + ': ' + ' '.join(vector))


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
