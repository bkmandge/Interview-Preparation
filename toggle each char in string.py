# using swapcase()
s = input("enter any string: ")
print(s.swapcase())


# w/o using swapcase()

def toggleChars(s):
    ans = ""
    for ch in s:
        if ch.isupper():
            ans = ans + ch.lower()
        else:
            ans = ans + ch.upper()
    return ans


# s = "KeePcODinG"
# print(toggleChars(s))
