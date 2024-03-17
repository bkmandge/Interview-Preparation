"""
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

"""

def areIsomorphic(s, t):
    if len(s) != len(t):
        return False

    hashMap = {}
    for i in range(len(s)):
        if s[i] in hashMap:
            if hashMap[s[i]] != t[i]:
                return False
        else:
            # If current character in t is already mapped to another character in s, return False
            if t[i] in hashMap.values():
                return False
            # Add mapping from current character in s to current character in t
            hashMap[s[i]] = t[i]
    return True


str1 = "aac"
str2 = "xxy"

if areIsomorphic(str1, str2):
    print("True")
else:
    print("False")


s = "egg"; t = "add"       # True
s = "foo"; t = "bar"        # False
s = "paper"; t = "title"    # True