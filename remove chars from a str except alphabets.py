"""                     Remove characters from a string except alphabets

s = "take12% *&u ^$#forward" -> takeuforward
s2 = "1.Python & 2.Java" -> PythonJava

"""

def removeSymbols(s):
    n = len(s)
    res = ""
    
    for i in range(n):
        ascii_val = ord(s[i])
        if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
            res = res + s[i]
      
    return res


s = "take12% *&u ^$#forward"

print(removeSymbols(s))
