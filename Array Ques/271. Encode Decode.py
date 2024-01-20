"""
Encode - Given a list of strings convert it into a single string
Decode - Given a single string convert it into list of strings


Time complexity- O(n) - n is total number of characters

"""


from typing import *

class Solution:
    def encode(self, strs: List[str]):  # strs:- lists of strings
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str: str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return res


ans = Solution()
print(ans.encode(['link', 'code', 'love', 'you']))
print(ans.decode('4#link4#code4#love3#you'))