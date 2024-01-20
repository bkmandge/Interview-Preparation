'''
128. Longest consecutive sequence (Hard)

find the length of longest consecutive sequence from unsorted array.

1. using sorting - O(NlogN) time & space complexities


1. create set & create longest var
2. Iterate through given array
    check if its start of sequence i.e. check if values have left neighbours,
    if they don't then create the length of sequence = 0

    compute length of current sequence & longest sequence
    :return longest sequence

        Visualise the real number line like & sort numbers
            [1, 2, 3, 4]    [100]       [200]
        <-------------------------------------------------->

Time & Mem. O(N)
'''

from typing import *

def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:  # n- 1 -> previous number i.e. neighbour number
            length = 0
            while (n + length) in numSet:  # n + length -> current number
                length += 1
            longest = max(length, longest)
    return longest


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
