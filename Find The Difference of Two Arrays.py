"""
                    Find The Difference of Two Arrays

nums1 = [1,2,3]
nums2 = [2,4,6]

o/p = [[1,3],[4,6]]


T.C. O(N + M) NEED TO TRAVERSE BOTH ARRAYS
S.C. O(N + M) NEED TO CREATE HASH SET FOR BOTH ARRAYS
"""


def findDifference(nums1, nums2):
    # remove duplicate elements from given arrays is any
    nums1 = set(nums1)
    nums2 = set(nums2)

    # create results hashset to store distinct integers from nums1 and nums2
    res1 = set()
    res2 = set()

    # iterate through nums1 array and check if element from nums1 is in nums2 if not then only add to res1.
    # do same process for nums2 array
    # finally return list of both hashsets

    for n in nums1:
        if n not in nums2:
            res1.add(n)

    for n in nums2:
        if n not in nums1:
            res2.add(n)

    return [list(res1), list(res2)]
