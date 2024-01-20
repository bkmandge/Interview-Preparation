"""
Solution:-

1. Sum Formula:- O(n) & O(1)
        Sn = N(N+1)/2 & Sum of all the array(Sa[]).
        res = (Sn-Sa[]) -> to find the Missing Number

2. Hashing:- O(n) & O(n)
        iterate over all the element up to the n and compare present element by creating the hash map of (n+1).

3. Bit manipulation(using XOR):- O(n) & O(1) No space overflow
        we take the XOR of given array and the first n natural no. .

"""

from typing import *


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# Sum Formula
def findMissing(list1, n):
    sum1 = n * (n + 1) // 2
    sum2 = sum(list1)
    print(sum1 - sum2)


findMissing(list1, 100)

list2 = [3, 0, 1]


class Solution:
    # Hashing
    def findMissing(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res


s1 = Solution()
print(s1.findMissing(list2))


class Solution:
    # Bit manipulation(using XOR)
    def findMissing(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res


list3 = [9,6,4,2,3,5,7,0,1]
s1 = Solution()
print(s1.findMissing(list3))


