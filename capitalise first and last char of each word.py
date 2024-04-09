# change first and last char of single word 
def capitaliseFirstLastChar(s):
    n = len(s)
    s = s[0:1].upper() + s[1:n-1] + s[n-1:n].upper()
    return s

# s = "keepcoding"
# print(capitaliseFirstLastChar(s))


# change first and last char of each word of sentence
def firstAndLast(s):
    lst = list(s)
    n = len(lst)
        
    for i in range(n):
        # k -> index of first char
        # i -> index of last char
        k = i
        while i < n and lst[i] != " ":
            i += 1
    
        ascii_first = ord(lst[k])
    
        if 97 <= ascii_first <= 122:
            lst[k] = chr(ascii_first - 32)
        
        ascii_last = ord(lst[i-1])
        if 65 <= ascii_last <= 90:
            lst[i-1] = chr(ascii_last + 32)
                
    return "".join(lst)


            
def FirstAndLast(s) :
    # Create an equivalent char array of given string
    lst = list(s);
    i = 0 ;
    while i < len(lst):
        # k stores index of first character and i is going to store index of last character.
        k = i;
        while (i < len(lst) and lst[i] != ' ') :
            i += 1;
        # Check if the character is a small letter If yes, then Capitalise
        if (ord(lst[k]) >= 97 and
            ord(lst[k]) <= 122 ):
            lst[k] = chr(ord(lst[k]) - 32);
        else :
            lst[k] = lst[k]
        if (ord(lst[i - 1]) >= 90 and
            ord(lst[i - 1]) <= 122 ):
            lst[i - 1] = chr(ord(lst[i - 1]) - 32);
        else :
            lst[i - 1] = lst[i - 1]
        i += 1
    return "" . join(lst);


s2 = "keep coding on a daily basis"
print(FirstAndLast(s2))
