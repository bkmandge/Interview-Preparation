# using ASCII values
def findSum(s):
    total = 0
    for ch in s:
        # find numbers using ascii value of curr char
        if ord(ch) >= 48 and ord(ch) <= 57:
            total = total + int(ch)
    return total


# using regex
import re
def findSum2(s):
    digits = re.findall(r'\d+', s)
    print(digits)
    return sum(map(int, digits))
    
    
# using isnumeric()
def findSum3(s):
    total = 0
    for ch in s:
        if ch.isnumeric():
            total += int(ch)
    return total
        

s = "4PREP2INSTAA6"
print(findSum2(s))
