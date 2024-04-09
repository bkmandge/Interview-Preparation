def removeSpecialChars(s):
    res = ""
    
    for ch in s:
        ascii = ord(ch) 
        # Finding the character whose ASCII value fall under this range
        if ((ascii >= ord('A') and ascii <= ord('Z')) or
            (ascii >= ord('a') and ascii <= ord('z')) or
            (ascii > ord('0') and ascii <= ord('9'))
            ):
            res =  res + ch
    return res


s = "keep_coding@you!"
print(removeSpecialChars(s))
