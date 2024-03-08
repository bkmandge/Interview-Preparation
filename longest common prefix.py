def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):      # iterate through first word
        for s in strs:              # iterate through rest all words
            if i == len(s) or s[i] != strs[0][i]:       #current words ith char is not equal to first words ith char
                return res
        res = res + strs[0][i]
    return res


strs = ["flower","flow","flight"]   # fl
strs2 = ["dog","racecar","car"]

print(longestCommonPrefix(strs))
print(longestCommonPrefix(strs2))   # ""

