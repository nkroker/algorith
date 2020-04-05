"""
    Imagine a series of a number from 1 to 10.
    
    1 2 3 4 5 6 7 8 9 10
    
    Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively. In other words, if a number is divisible
    by 3, it is substituted with fizz; if a number is divisible by 5, it is substituted with buzz. If a number is simultaneously
    a multiple of 3 AND 5, the number is replaced with "fizz buzz." In essence, it emulates the famous children game
    "fizz buzz".

"""

from termcolor import colored

# The fastast way of doing this
def fiz_buzz_fast(series):
    for element in series:
        if element%15 == 0:
            print(element, " - Fizz Buzz")
        elif element%3 == 0:
            print(element, " - Fizz")
        elif element%5 == 0:
            print(element, " - Buzz")
        else:
            print(element)


# Slow method of doing this cause it's linear
def fiz_buzz_slow(series):
    for element in series:
        if element%3 == 0 and element%5 == 0:
            print(element, " - Fizz Buzz")
        elif element%3 == 0:
            print(element, " - Fizz")
        elif element%5 == 0:
            print(element, " - Buzz")
        else:
            print(element)

series = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


print("\nSlow appproach for testing this using linear method:")
fiz_buzz_slow(series)


print("\n\nFast appproach for testing this using non linear method:")
fiz_buzz_fast(series)
