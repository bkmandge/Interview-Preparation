# Generate fibonacci sequence
"""
1. Create fib_series = [0, 1]
2. loop till length of fib_series is < given num
3. add last element + second last element of fib_series
4. append this new addition to end of fib_series

"""


def fibonacci_sequence(num):
    fib_series = [0, 1]
    while len(fib_series) < num:
        next_seq = fib_series[-1] + fib_series[-2]
        fib_series.append(next_seq)
    return fib_series


print(fibonacci_sequence(5))
print(fibonacci_sequence(8))
