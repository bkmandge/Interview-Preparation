                    # Recursive Range Function

# returns sum of all previous numbers from given number(including this also)
def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)


# returns sum of 1 + 2 + 3 + 4 + 5
print(recursiveRange(5))

# returns sum of 1 + 2 + 3 + 4 + 5 + 6
print(recursiveRange(6))
