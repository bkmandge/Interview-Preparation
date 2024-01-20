'''
                    1898. Maximum Number of Removable Chars (Medium)

-> p = ab is a subsequence of s = abcacb, even after removing chars from index [3, 1, 0]
-> after removing oth index char p is not subsequence of s, so max k is 2

-> Binary Search -> on removable characters [3, 1, 0]
Time: O(N.logK) -> n is len of chars,
        k -> number of removable indices, binary search on removable indices so, logK

1. helper functions() -> to check if p is subsequence of s
2. binary search()

'''

from typing import *


class Solution:
    def maximumRemovables(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(s, subseq):
            i1, i2 = 0, 0

            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            return i2 == len(subseq)

        res = 0
        l, r = 0, len(removable) - 1

        while l <= r:
            mid = (l + r) // 2

            removed = set(removable[: mid + 1])  # chars removed from s
            if isSubseq(s, p):
                res = max(res, mid + 1)  # returning number of removable chars mid + 1, index starts from 0 so mid + 1
                l = mid + 1
            else:
                r = mid - 1
        return res


result = Solution()
s = 'abcacb'
p = 'ab'
removable = [3, 1, 0]
print(result.maximumRemovables(s, p, removable))

