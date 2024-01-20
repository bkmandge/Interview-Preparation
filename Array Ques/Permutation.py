"""
Permutation:- same characters but in different order
"""


def permutation(list1: int, list2: int):
    if len(list1) == len(list2):
        list1.sort()
        list2.sort()

        if list1 == list2:
            return True
        else:
            return False

    return False


list1 = ['a', 'c', 'b']
list2 = ['a', 'b', 'c']

print(permutation(list1, list2))
