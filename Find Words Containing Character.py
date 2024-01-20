"""
                            Find Words Containing Character
Input: words = ["leet","code"], x = "e"
Output: [0,1]

Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0, 2]

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: []
"""

from typing import *
def findWordsContaining(words: List[str], x: str) -> List[int]:
    idx = []
    for i in range(len(words)):
        if x in words[i]:
            idx.append(i)
    return idx


words = ["abc","bcd","aaaa","cbc"]
x = 'z'

print(findWordsContaining(words, x))
