def maxDepth(s: str) -> int:
    # count nested "(" till underlined char
    res = 0
    curDepth = 0

    for char in s:
        if char == "(":
            curDepth += 1
        elif char == ")":
            curDepth -= 1
        res = max(res, curDepth)
    return res


s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))
