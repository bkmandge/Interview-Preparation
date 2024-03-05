"""
                            Find Words Containing Character
Input: words = ["leet","code"], x = "e"
Output: [0,1]

Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0, 2]

Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
"""

from typing import *
def findWordsContaining(words: List[str], x: str) -> List[int]:
    n = len(words)
    idx = []
    for i in range(n):
        if x in words[i]:
            idx.append(i)
    return idx


words = ["abc","bcd","aaaa","cbc"]
x = 'z'

print(findWordsContaining(words, x))
