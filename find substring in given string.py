def findSubstring(s, t):
    mainS = len(s)
    subS = len(t)
    
    for i in range(mainS - subS + 1):
        match = True
        for j in range(subS):
            if s[i + j] != t[j]:
                match = False
                break
        
        if match is True:
            return i  # returns starting index of substring in main string
    return -1


s = "abcde"
t = "cde"

print(findSubstring(s, t))


def strStr(haystack, needle):
    if not needle:
        return 0

    if not haystack:
        return -1

    n = len(needle)
    h = len(haystack)

    # iterates through the haystack string using a sliding window
    #  window size is equal to the needle string size
    # haystack[i : i + n] i -> starting index
    # i + n -> ending index of the substring you want to extract
    for i in range(h - n + 1):
        if haystack[i: i + n] == needle:
            return i
    return -1


haystack1 = "sadbutsad"
needle1 = "sad"  # 0
haystack2 = "leetcode"
needle2 = "leeto"  # -1



