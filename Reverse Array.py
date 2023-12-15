# Reverse given array / list

lst = [6, 11, 7, 4, 8, 20]  # [20, 8, 4, 7, 11, 6]


def reverse_list(list1):
    start = 0
    end = len(list1) - 1
    while start < end:
        list1[start], list1[end] = list1[end], list1[start]
        start += 1
        end -= 1
    return list1


print("Original list: ", lst)
print("Reversed list: ", reverse_list(lst))
