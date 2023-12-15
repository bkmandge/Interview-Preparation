# Find trailing zeroes (zeroes at the end) in given number's factorial
"""
1. Given number >= 5, as there will be no zeroes in numbers below 5
2. Divide given num by 5, add rec'd quotient to zero_counter variable
3. Divide given num by 5, to get next num for next iteration

"""


def trailing_zeroes(num):
    zero_counter = 0
    while num >= 5:
        zero_counter += num // 5
        num = num // 5
    return zero_counter


print(trailing_zeroes(30))
