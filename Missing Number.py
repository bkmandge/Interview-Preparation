# Find missing number in given list
# Subtract given list's addition from original list

def missing_number(lst, n):
    sum1 = n * (n + 1) // 2  # 5 * (5 + 1) // 2 = 15
    sum2 = sum(lst)   # 1+ 2 + 3 + 5 = 11
    print(sum1 - sum2)


list1 = [1, 2, 3, 5]
missing_number(list1, 5)

