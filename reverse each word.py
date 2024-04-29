def reverseWords(s):
    n = len(s)
    res = ""
    
    for i in range(n - 1, -1, -1):
        res += s[i]
    return res


# using slicing
def reverseWords2(s):
    return s[::-1]
        

# using stack
def reverseWords2(s):
    n = len(s)
    stack = []
    
    for i in range(n):
        stack.append(s[i])
    
    # rev string to store output
    rev = ""
    temp = ""
    
    while len(stack) > 0:
        if stack[-1].isalpha:
            temp = temp + stack.pop()
        else:
            rev = " " + temp + rev
            temp = ""
            stack.pop()

    # if temp is not empty, add temp to rev at the front

    if temp != "":
        rev = temp + rev
    
    return rev


# s = "Hello world"
# print(reverseWords(s))


    