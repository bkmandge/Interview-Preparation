# Calculate sum of given digits

# Iterative way
def sum_digits1(num):
    if num < 0:
        return 0
    ans = 0
    while num != 0:
        rem = num % 10
        num = num // 10
        ans = ans + rem
    return ans


print(sum_digits1(-123))


# Recursive way
def sum_digits(n):
    assert n == int(n) and n >= 0, 'Enter positive number only!'
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)


# print(sum_digits(-123))
# print(sum_digits(258))