# Reverse given integer
# 17 -> 71, 258 -> 852,


def reverse_integer(num):
    ans = 0
    while num:
        rem = num % 10
        num = num // 10
        ans = ans * 10 + rem
    return ans


number = int(input("enter any number: "))
print("Original integer: ", number)
print("Reverse integer: ", reverse_integer(number))

