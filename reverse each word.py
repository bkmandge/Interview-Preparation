def reverseWords(s):
    ans = ""
    
    wordList = s.split()
    
    for i in wordList:
        ans = i[::-1]
        print(ans, end=" ")


# s = "Geeks for Geeks"
# reverseWords(s)

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


s = "Geeks for Geeks"
print(reverseWords2(s))


    