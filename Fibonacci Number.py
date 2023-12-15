# Calculate fibonacci sequence of given number

def fibonacci(num):
    if num in [0, 1]:
        return num
    while num:
        return fibonacci(num - 1) + fibonacci(num - 2)


# number = int(input("Enter any number: "))
# print("Fibonacci calculation:", fibonacci(number))

# 5 -> 0, 1, 1, 2, 3
# 6-> 0, 1, 1, 2, 3, 5


def fib_sequence(num):
    fib_series = [0, 1]

    while len(fib_series) < num:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return fib_series


number = int(input("Enter any number: "))
print("Fibonacci series: ", fib_sequence(number))
