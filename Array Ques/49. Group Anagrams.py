"""
                            49. Group Anagrams

I/P: strs = ["eat", "tea", "tan", "ate", "mat", "bat"]
O/P: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

1. by sorting each string - O(m.nlogn) -> m - length of all i/p str, n - avg length of each i/p str, logn - sorting time
                            read as -> m times n log n
2. by using hashmap(key-value pairs) - O(m.n.26 letters) -> reduces to O(m.n)
    ***from collections import defaultdict***
            Defining a dictionary with values as a list

    1. create hashmap to count char to list of anagrams
    2. loop through given string -> create blank count_array
        loop through each string char by char
            subtract ascii value original alphabets with present char to get its count
        append count to count tuple(count used as key)
    3. return values

"""
from typing import *
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)

        return result.values()


ans = Solution()

print(ans.groupAnagrams(["eat", "tea", "tan", "ate", "mat", "bat"]))