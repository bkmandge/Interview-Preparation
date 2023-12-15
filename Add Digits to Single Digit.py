# Add digits and return single digit
# 17 -> 1 + 7 = 8, 258 -> 2 + 5 + 8 = 15 -> 1 + 5 = 6


def add_digits(num):
    while num > 9:
        ans = 0
        rem = 0
        while num:
            rem = num % 10
            num = num // 10
            ans = ans + rem
        num = ans
    return num


# print(add_digits(258))


