from collections import defaultdict


def findTheDifference(s: str, t: str) -> str:
    # create hashMap of string t
    tCount = defaultdict(int)        
    for char in t:
        tCount[char] += 1
    
    # iterate in s and delete char's frequency from hashMap of t
    for char in s:
        tCount[char] = tCount[char] - 1
    
    # now check left out char in t with count == 1 and return that char
    for char, freq in tCount.items():
        if freq == 1:
            return char


# s = ""; t = "y"     # y
s = "abcd"; t = "abcde"     # e

print(findTheDifference(s, t))
