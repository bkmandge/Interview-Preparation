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

    