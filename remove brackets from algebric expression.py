def removeBrackets(s):
    ans = ""
    for ch in s:
        if ch not in "[{()}]":
           ans = ans + ch 
    return ans


# using ASCII values
def removeBrackets2(s):
    res = ""
    for ch in s:
        if (ord(ch) == 41 or ord(ch) == 40 
            or ord(ch) == 91 or ord(ch) == 93 
            or ord(ch) == 123 or ord(ch) == 125):
           # res = res + ch     -> to get () [] {}
           pass
        else:
            res = res + ch      # to get algebric expression except brackets
    return res 
    

s = "(a-b)+[c*d]+{e/f}"
print(removeBrackets2(s))        
