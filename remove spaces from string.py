"""                 Remove Spaces from a String

s = "Take you forward"  -> Takeyouforward

T.C. O(N)
S.C. O(1)
"""

def removeSpaces(s):
    res = []

    for char in s:
        if char != " ":
            res.append(char)
    res.append('\0')    # append \0 as null char at the end of string
    return ''.join(res)


s = "Take you forward"
print(removeSpaces(s))

s = "Take you forward"
print(removeSpaces(s))


