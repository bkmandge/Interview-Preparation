"""                     Find Non-repeating characters of a String

s = "google"  -> l, e
s2 = "yahoo"  -> y, a, h

"""

def nonRepeatingChars(s):
    n = len(s)
    hashArray = [0] * n   # declare hashArray
    
    
    # count all chars frequencies
    for i in range(n):
        if s[i] != '-':
            hashArray[i] = 1   # creating hashArray with count 1      
            for j in range(i + 1, n):  # to avoid revisiting chars
                if s[i] == s[j]:  # counts frequncy of duplicate chars
                    hashArray[i] += 1
                    # Mark the visited character
                    s = s[:j] + '-' + s[j + 1:] 
        
    # printing non-repeating chars
    for i in range(n):
        if hashArray[i] == 1 and hashArray[i] != " " and hashArray[i] != " ":
            print(s[i])


s = "google"  # l, e
s2 = "yahoo"  # y, a, h

# nonRepeatingChars(s)
nonRepeatingChars(s2)