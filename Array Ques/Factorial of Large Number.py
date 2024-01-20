"""                     Calculating factorial:-
1. Recursion - calling factorial function repeatedly
2. Iteration - while loop
"""


def factorial(num):
    assert num >= 0 and num == int(num), 'Enter positive integer only!'
    if num in [0, 1]:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input('Enter any number: '))
print(factorial(num))

# Iteration - while loop

def calculate_fact(number):
    fact = 1
    while number:
        fact = fact * number
        number -= 1
    return fact


number = int(input('Enter any number: '))
print(calculate_fact(number))
