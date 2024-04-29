"""                 Remove Spaces from a String


"""
# count spaces and replace those with empty string ""
def removeSpaces(s):
    count = 0
    
    for ch in s:
        if ch == " ":
            count += 1
    
    for i in range(count):
        s = s.replace(" ", "")
    return s


# using extra space
def removeSpaces2(s):
    res = []

    for ch in s:
        if ch != " ":
            res.append(ch)
    return ''.join(res)


s = "keep coding continue"
print(removeSpaces2(s))
