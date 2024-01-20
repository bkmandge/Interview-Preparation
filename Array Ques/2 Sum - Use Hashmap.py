"""
                                Two Sum (Easy)
WAP to find all pairs of integers whose sum is to a given number i.e. Target, return their indices
Note:- pairs has to be distinct

1. Using Brute force algo:- Time & space complexity:- O(n2)
2. Using Hashmap / Dictionary:- O(n):-
    1. declare empty hashmap - prevMap = {}
    2. loop through given list, calculate difference of value
    3. check if difference element is in prevMap, yes then return first & second indices
    4. else add index to prevMap

"""

from typing import *


def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)


myList = [1, 2, 3, 2, 3, 4, 5, 6]

# 0 6, 1 5, 2 4, 3 5
# findPairs(myList, 6)


def twoSum(nums: List[int], target: int)-> int:
    seen = {}  # val : index

    for index, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], index]

        seen[num] = index


customList = [2, 1, 5, 3, 15]
target = 6
print(twoSum(customList, target))
