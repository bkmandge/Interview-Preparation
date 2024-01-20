"""
Palindrome:- Order of elements is same in Reverse == original

1. declare two pointers l & r to 0 & last element of list
2. check if both pointers are not same & return False
3. else increment left pointer & decrease right pointer by 1


Test cases:-
[] - True
[1] - True
[1, 2] - False
[1, 2, 1] - True
[1, 2, 2, 1] - True
['a', 'a'] - True
['a', 'b'] - False
['a', 'b', 'a'] - True
['a', 'b', 'c', 'a'] - False

"""

from array import array

customArray = array('i', [1, 2, 2, 1])

print(customArray)


def isPalindrome(array1):
    l, r = 0, len(array1) - 1
    while l <= r:
        if array1[l] != array1[r]:
            return False
        l += 1
        r -= 1
    return True


print(isPalindrome(customArray))
