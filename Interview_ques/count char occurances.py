"""                     Count given character's frequency


"""
# Using hash array
def countFrequency(s, char):
    n = len(s)
    hashArray = [0] * 26

    for i in range(n):
        hashArray[ord(s[i]) - ord('a')] += 1
    # print(hashArray)

    return hashArray[ord(char) - ord('a')]


# using hash dict / hashmap

def countFrequency2(s, char):
    n = len(s)
    hashDict = {}

    # creating hashmap with count
    for i in range(n):
        hashDict[s[i]] = 1 + hashDict.get(s[i], 0)
    # print(hashDict)

    if char in hashDict:        # if key is in hashmap return its count/value
        return hashDict[char]


s = "abcdaaacc"
char1 = 'b'    # 1
char2 = 'z'     # 0

print(countFrequency2(s, char1))
# print(countFrequency(s, char2))
