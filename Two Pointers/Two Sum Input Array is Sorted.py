"""

WAP to find two numbers that add up to given specific number.
Note:-
1. array is sorted in ascending order.
2. Same element should not be twice
3. Indices should start from 1 not from 0 & returning indices must be index1 < index2

Solution:-
1. Using Brute force algo :- O(n2)
2. Using Left & Right pointers:- O(n) -> need to iterate only once through entire given sorted array.
   L & R pointers don't cross each other, so no extra memory is required.

1. declare l & r pointers
2. while l < r: add l + r values to sum
3. check if sum > given target, if yes then decrease r pointer by 1
4. elif check opposite & increase l pointer by 1
5. else return indices of l & r by adding 1 to both
6. finally return [] to get in list form

"""
from typing import *


def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]  # as 0 based indexing need to return by adding 1 to index
    return []


customList = [1, 3, 4, 5, 7, 10, 11]
print(twoSum(customList, 9))

