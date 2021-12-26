#!/usr/bin/python -tt

# Gather our code in a main() function
def main():
    import random   # import the module for calling random numbers

# this program is a random kindness generator
# You can define your own functions using "def"
# "def getAnswer()" defines our function
# The getAnswer() function in this program has a parameter called "answerNumber"
# The parameter is a variable we pass into our function.

# A "return" statement pass the result of the function back to the caller.
    # if there is no result to the function the "return" statement give you a "None" value.
    # "None" represents the absence of a value.

    def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'You look great today.'
        elif answerNumber == 2:     # "elif" means "else if", is used if you need multiple if instances.
            return 'You’re like sunshine on a rainy day.'
        elif answerNumber == 3:
            return 'Being around you makes everything better!'
        elif answerNumber == 4:
            return 'Colors seem brighter when you’re around.'
        elif answerNumber == 5:
            return 'You’re wonderful.'
        elif answerNumber == 6:
            return 'You’re one of a kind!'
        elif answerNumber == 7:
            return 'You’re irresistible when you blush.'
        elif answerNumber == 8:
            return 'You’re someone’s reason to smile.'
        elif answerNumber == 9:
            return 'You’re really something special.'
    r = random.randint(1, 9)  # generate a random integer between 1 and 9.
    kindness = getAnswer(r)   # we call our function, and we pass our parameter "r"
    print(kindness)

# Standard boilerplate to call the main() function to begin the program.
# copy and paste this stuff everywhere.


if __name__ == '__main__':
    main()
