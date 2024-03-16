"""                     Determine if two strings are close or not
Operation 1: Swap any two existing characters.
abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
"""

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    # create two hashmaps, add count of each char in it
    count1 = {}
    count2 = {}

    for char in word1:
        count1[char] = count1.get(char, 0) + 1
    
    for char in word2:
        count2[char] = count2.get(char, 0) + 1
    
    # check if keys of both hashmaps are same or not
    if set(count1.keys()) != set(count2.keys()):
        return False

    # if count of chars in sorted hashmaps are equal or not
    return sorted(count1.values()) == sorted(count2.values())


# word1 = "abc"; word2 = "bca"
word1 = "a"; word2 = "aa"   # It is impossible to attain word2 from word1, or vice versa, in any number of operations.

print(closeStrings(word1, word2))

