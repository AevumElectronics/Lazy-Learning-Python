#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    # The function "fortytwo" divide the number 42 by "divideBy".
    # We can't divide by zero and if we do the program crash.
    # To avoid that we use "try" and "except"
    # The "try" block lets you test a block of code for errors.
    # The "except" block lets you handle the error.

    def fortytwo(divideBy):
        try:
            return 42 / divideBy
        except ZeroDivisionError:  # "ZeroDivisionError" is the error we get dividing by zero
            print('Error: Invalid argument.')

    print(fortytwo(2))  # The function returns 42/2.
    print(fortytwo(-12))
    print(fortytwo(0))  # We can't divide by 0, so we get into the "except".
                        # The print function prints both the error message and the value of returned value
                        # Which is "None" in this case
    print(fortytwo(1))


# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
