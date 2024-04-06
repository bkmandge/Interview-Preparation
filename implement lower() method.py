def lower(char):
    # to check given char is capital char:- ord(char) < ord('a') or check ord(char) > 'z
    # map upper case to lower case char -> ord(char) - ord('A')
    # and add to lower case char ord('a) -> ord('a') + ord(char) - ord('A')
    # convert back to string representation
    if ord(char) < ord('a'):
        return chr(ord('a') + ord(char) - ord('A'))
    else:
        return char
    

char = "M" 
char2 = "B"       
char3 = "K"

print(lower(char))
