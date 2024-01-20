"""
Anagram:- Creating new string using same characters of previous string
          Both strings must have same length, same characters in different order
          eg:- anagram == nagaram

1. Using Hashmap:-
    1. check length of both strings, if not return False
    2. create two hashmaps
    3. build hashmaps -> iterate through given strings char by char & adding their count to above hashmaps
    4. iterate through first hashmap & check if count of each char is same or not in other hashmap

2. Using Counter:- built-in data structure which is hashmap, counts chars automatically
                        return Counter(s) == Counter(t)

3. Using Sorting:- return sorted(s) == sorted(t)

"""
from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #creating two hashmaps
        countS, countT = {}, {}

        #iterating through given strings char by char & adding their count to above hashmaps(building hashmap)
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #iterate through hashmap & check if count of each char is same or not
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True


s1 = Solution()
print(s1.isAnagram('rat', 'car'))

8