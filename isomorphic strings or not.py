def areIsomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    char_map = {}
    for i in range(len(str1)):
        if str1[i] in char_map:
            if char_map[str1[i]] != str2[i]:
                return False
        else:
            if str2[i] in char_map.values():
                return False
            char_map[str1[i]] = str2[i]
    return True


str1 = "aac"
str2 = "xxy"

if areIsomorphic(str1, str2):
    print("True")
else:
    print("False")
