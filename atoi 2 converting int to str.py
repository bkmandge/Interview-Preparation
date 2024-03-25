# another way

def myAtoi(s):
    n = len(s)
    res = 0
    for i in range(n):
        res = res * 10 + (ord(s[i]) - ord('0'))
    return res


string = "89789"

print(myAtoi(string))