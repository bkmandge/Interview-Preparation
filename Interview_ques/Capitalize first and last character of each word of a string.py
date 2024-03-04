"""                 Capitalize first and last character of each word of a string

s = "take u forward is awesome" -> “TakE U ForwarD IS AwesomE”

s2 = "Take u Forward is Awesome" -> “TakE U ForwarD IS AwesomE”

"""

def capitalizeWord(s):
    n = len(s)
    s_list = list(s)
    
    for i in range(n):
        if i == 0 or (i == n - 1 and ord(s[i]) >= 97):
          # Convert first and last index character to uppercase if initially the string character is in lowercase 
            s_list[i] = chr(ord(s[i]) - 32)
        elif s[i] == " ":
            # Converting characters present before and after space to uppercase
            if ord(s[i - 1]) - 32 >= 65:
                s_list[i - 1] = chr(ord(s[i - 1]) - 32)
            if ord(s[i + 1]) - 32 >= 65:
                s_list[i + 1] = chr(ord(s[i + 1]) - 32)  

    # Convert the list back to a string and return
    return "".join(s_list)
            
            
s = "take u forward is awesome" 
print(capitalizeWord(s))
s2 = "Take u Forward is Awesome"

