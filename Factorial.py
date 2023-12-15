# Iterative way

def calculate_factorial(n):
    assert n == int(n) and n >= 0, 'Number must be positive!'
    if n in [0, 1]:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# print(calculate_factorial(5))


# Recursive way

def calculate_factorial2(n):
    assert n == int(n) and n >= 0, 'Number must be positive!'
    if n in [0, 1]:
        return 1
    else:
        return n * calculate_factorial(n - 1)


print(calculate_factorial2(0))

